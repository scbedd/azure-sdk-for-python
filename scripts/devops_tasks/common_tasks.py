#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Below are common methods for the devops build steps. This is the common location that will be updated with
# package targeting during release.

import glob
from pathlib import Path
from subprocess import check_call, CalledProcessError
import os
import errno
import shutil
import sys
import logging
import ast
import textwrap
import io
import re

logging.getLogger().setLevel(logging.INFO)

OMITTED_CI_PACKAGES = ["azure-mgmt-documentdb", "azure-servicemanagement-legacy"]
MANAGEMENT_PACKAGE_IDENTIFIERS = [
    "mgmt",
    "azure-cognitiveservices",
    "azure-servicefabric",
    "azure-nspkg",
]
MAJOR_VERSION_REGEX = re.compile("Python\s\:\:\s(?P<languageClassifier>[\d])[\.\d]*'")

def log_file(file_location, is_error=False):
    with open(file_location, "r") as file:
        for line in file:
            sys.stdout.write(line)
        sys.stdout.write("\n")
        sys.stdout.flush()


def read_file(file_location):
    str_buffer = ""
    with open(file_location, "r") as file:
        for line in file:
            str_buffer += line
    return str_buffer


def cleanup_folder(target_folder):
    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            logging.error(e)


# helper functions
def clean_coverage(coverage_dir):
    try:
        os.mkdir(coverage_dir)
    except OSError as e:
        if e.errno == errno.EEXIST:
            logging.info("Coverage dir already exists. Cleaning.")
            cleanup_folder(coverage_dir)
        else:
            raise

def parse_setup_classifers(setup_path):
    setup_filename = os.path.join(setup_path, 'setup.py')
    mock_setup = textwrap.dedent('''\
    def setup(*args, **kwargs):
        __setup_calls__.append((args, kwargs))
    ''')
    parsed_mock_setup = ast.parse(mock_setup, filename=setup_filename)
    with io.open(setup_filename, 'r', encoding='utf-8-sig') as setup_file:
        parsed = ast.parse(setup_file.read())
        for index, node in enumerate(parsed.body[:]):
            if (
                not isinstance(node, ast.Expr) or
                not isinstance(node.value, ast.Call) or
                not hasattr(node.value.func, 'id') or
                node.value.func.id != 'setup'
            ):
                continue
            parsed.body[index:index] = parsed_mock_setup.body
            break

    fixed = ast.fix_missing_locations(parsed)
    codeobj = compile(fixed, setup_filename, 'exec')
    local_vars = {}
    global_vars = {'__setup_calls__': []}
    current_dir = os.getcwd()
    working_dir = os.path.dirname(setup_filename)
    os.chdir(working_dir)
    exec(codeobj, global_vars, local_vars)
    os.chdir(current_dir)
    _, kwargs = global_vars['__setup_calls__'][0]

    classifiers = kwargs['classifiers']
    return classifiers

def parse_major_classifiers(classifier_set):
    major_versions = []
    for classifier in classifier_set:
        result = re.search(MAJOR_VERSION_REGEX, classifier)
        if result and result.group('languageClassifier'):
            major_versions.append(result.group('languageClassifier'))
    return set(major_versions)

def filter_for_compatibility(package_set):
    running_major_version = sys.version_info[0]
    collected_packages = []
    for pkg in package_set:
        pkg_classifiers = parse_setup_classifers(pkg)
        supported_major_versions = parse_major_classifiers(pkg_classifiers)

        if running_major_version in supported_major_versions:
            collected_packages.append(pkg)

    return collected_packages

# this function is where a glob string gets translated to a list of packages
# It is called by both BUILD (package) and TEST. In the future, this function will be the central location
# for handling targeting of release packages
def process_glob_string(glob_string, target_root_dir):
    if glob_string:
        individual_globs = glob_string.split(",")
    else:
        individual_globs = "azure-*"
    collected_top_level_directories = []

    for glob_string in individual_globs:
        globbed = glob.glob(
            os.path.join(target_root_dir, glob_string, "setup.py")
        ) + glob.glob(os.path.join(target_root_dir, "sdk/*/", glob_string, "setup.py"))
        collected_top_level_directories.extend([os.path.dirname(p) for p in globbed])

    # dedup, in case we have double coverage from the glob strings. Example: "azure-mgmt-keyvault,azure-mgmt-*"
    collected_directories = list(set(collected_top_level_directories))

    # if we have individually queued this specific package, it's obvious that we want to build it specifically
    # in this case, do not honor the omission list
    if len(collected_directories) == 1:
        return filter_for_compatibility(collected_directories)
    # however, if there are multiple packages being built, we should honor the omission list and NOT build the omitted
    # packages
    else:
        allowed_package_set = remove_omitted_packages(collected_directories)
        logging.info("Target packages after filtering by omission list: {}".format(allowed_package_set))

        pkg_set_ci_filtered = filter_for_compatibility(allowed_package_set)
        logging.info("Target packages after ci compatibility filter: {}".format(list(set(allowed_package_set) - set(pkg_set_ci_filtered))))
        
        exit(1)
        return sorted(pkg_set_ci_filtered)

def remove_omitted_packages(collected_directories):
    return [
        package_dir
        for package_dir in collected_directories
        if os.path.basename(package_dir) not in OMITTED_CI_PACKAGES
    ]


def run_check_call(
    command_array,
    working_directory,
    acceptable_return_codes=[],
    run_as_shell=False,
    always_exit=True,
):
    try:
        if run_as_shell:
            logging.info(
                "Command Array: {0}, Target Working Directory: {1}".format(
                    " ".join(command_array), working_directory
                )
            )
            check_call(" ".join(command_array), cwd=working_directory, shell=True)
        else:
            logging.info(
                "Command Array: {0}, Target Working Directory: {1}".format(
                    command_array, working_directory
                )
            )
            check_call(command_array, cwd=working_directory)
    except CalledProcessError as err:
        if err.returncode not in acceptable_return_codes:
            logging.error(err)  # , file = sys.stderr
            if always_exit:
                exit(1)
            else:
                return err
