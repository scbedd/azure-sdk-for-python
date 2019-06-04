#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Normally, this module will be executed as referenced as part of the devops build definitions.
# An enterprising user can easily glance over this and leverage for their own purposes.

import argparse
import sys
from pathlib import Path
import os

from common_tasks import process_glob_string, run_check_call

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..'))
dev_setup_script_location = os.path.join(root_dir, 'scripts/dev_setup.py')

def execute_pylint(targeted_packages, optional_arguments):
    #pylint --output-format=parseable --rcfile {toxinidir}/../../../pylintrc --exit-zero {toxinidir}/azure

    command_array = ['pylint', '--exit-zero', '-rn', '-j', '0', '--rcfile', os.path.join(root_dir, 'pylintrc')]
    command_array.extend(optional_arguments)
    command_array.extend([os.path.join(targeted_package, 'azure') for targeted_package in targeted_packages])

    run_check_call(command_array, root_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Install Dependencies, Install Packages, Test Azure Packages, Called from DevOps YAML Pipeline')
    parser.add_argument(
        '-p',
        '--python-version',
        dest = 'python_version',
        default = 'python',
        help = 'The name of the python that should run the build. This is for usage in special cases like the "Special_Python_Distro_Tests" Job in /.azure-pipelines/client.yml. Defaults to "python"')

    parser.add_argument(
        'glob_string',
        nargs='?',
        help = ('A comma separated list of glob strings that will target the top level directories that contain packages.'
                'Examples: All = "azure-*", Single = "azure-keyvault", Targeted Multiple = "azure-keyvault,azure-mgmt-resource"'))

    parser.add_argument(
        '--service',
        help=('Name of service directory (under sdk/) to test.'
              'Example: --service applicationinsights'))

    args = parser.parse_args()

    # We need to support both CI builds of everything and individual service
    # folders. This logic allows us to do both.
    if args.service:
        service_dir = os.path.join('sdk', args.service)
        target_dir = os.path.join(root_dir, service_dir)
    else:
        target_dir = root_dir

    targeted_packages = process_glob_string(args.glob_string, target_dir)

    optional_arguments = []

    execute_pylint(targeted_packages, optional_arguments)
