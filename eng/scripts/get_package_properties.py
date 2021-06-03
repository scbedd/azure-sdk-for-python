import argparse
import sys
import glob
import os
import re
import pdb

sys.path.append(os.path.join('scripts', 'devops_tasks'))
from common_tasks import get_package_properties

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get package version details from the repo')
    parser.add_argument('-s', '--search_path', required=True, help='The scope of the search')
    args = parser.parse_args()

    seen_exception = 0

    for root, dirs, files in os.walk(args.search_path):
        if re.search(r"sdk[\\/][^\\/]+[\\/][^\\/]+$", root):
            for filename in files:
                if os.path.basename(filename) == "setup.py":
                    #if os.path.basename(root) != 'azure-mgmt' and os.path.basename(root) != 'azure' and os.path.basename(root) != 'azure-storage' and os.path.basename(root) != 'tests':
                    try:
                        print("entering {}".format(filename))
                        pkgName, version, is_new_sdk, setup_py_path = get_package_properties(root)
                        print("{0} {1} {2} {3}".format(pkgName, version, is_new_sdk, setup_py_path))
                    except:
                        # Skip setup.py if the package cannot be parsed
                        print("excepting against {}".format(filename))
                        seen_exception

            
                            
                        
                        