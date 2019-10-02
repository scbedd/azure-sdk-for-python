#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute pylint within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_call, CalledProcessError
import argparse
import os
import logging
import sys
from prep_sphinx_env import get_package_details
from pkg_resources import Requirement
import ast
import os
import textwrap
import io
import zipfile
import shutil

logging.getLogger().setLevel(logging.INFO)

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))
ci_doc_dir = os.path.join(root_dir, '_docs')

def in_ci():
    return os.getenv('TF_BUILD', False)

def move_output_and_zip(target_dir, package_dir):
    pkg_name, pkg_version = get_package_details(os.path.join(package_dir, 'setup.py'))
    individual_zip_location = os.path.join(ci_doc_dir, "{}.zip".format(pkg_name))

    new_zip = zipfile.ZipFile(individual_zip_location, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            new_zip.write(os.path.join(root, file))

def cleanup_previous_artifacts():
    if os.path.exists(ci_doc_dir):
        shutil.rmtree(ci_doc_dir)
    os.mkdir(ci_doc_dir)

def sphinx_build(target_dir, output_dir):
    command_array = [
                "sphinx-build",
                "-b",
                "html",
                target_dir,
                output_dir
            ]

    try:
        logging.info("Sphinx build command: {}".format(command_array))
        check_call(
            command_array
        )
    except CalledProcessError as e:
        logging.error(
            "sphinx-apidoc failed for path {} exited with error {}".format(
                args.working_directory, e.returncode
            )
        )
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run sphinx-build against target folder. Zips and moves resulting files to a root location as well."
    )

    parser.add_argument(
        "-w",
        "--workingdir",
        dest="working_directory",
        help="The unzipped package directory on disk. Usually {distdir}/unzipped/",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--outputdir",
        dest="output_directory",
        help="The output location for the generated site. Usually {distdir}/site",
        required=True,
    )

    parser.add_argument(
        "-r",
        "--root",
        dest="package_root",
        help="",
        required=True,
    )

    parser.add_argument(
        "--inci",
        dest="in_ci",
        action="store_true",
        default=False
    )

    args = parser.parse_args()

    cleanup_previous_artifacts()

    output_dir = os.path.abspath(args.output_directory)
    target_dir = os.path.abspath(args.working_directory)
    package_dir = os.path.abspath(args.package_root)

    sphinx_build(target_dir, output_dir)

    if in_ci() or args.in_ci:
        move_output_and_zip(output_dir, package_dir)
