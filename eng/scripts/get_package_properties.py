import argparse
import sys
import glob
import os
import re
import pdb

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))
sys.path.append(os.path.join('scripts', 'devops_tasks'))

from common_tasks import get_package_properties

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get package version details from the repo')
    parser.add_argument('-s', '--search_path', required=True, help='The scope of the search')
    args = parser.parse_args()

    found_setup_folders = []

    for root, dirs, files in os.walk(os.path.abspath(args.search_path)):
        if re.search(r"sdk[\\/][^\\/]+[\\/][^\\/]+$", root):
            if "setup.py" in files:
                found_setup_folders.append(root)

    for setup_path in found_setup_folders:
        try:
            pkgName, version, is_new_sdk, setup_py_path = get_package_properties(setup_path)
            print("{0} {1} {2} {3}".format(pkgName, version, is_new_sdk, os.path.relpath(setup_py_path, root_dir)))
        except Exception as e:
            # Skip setup.py if the package cannot be parsed
            pass
                            