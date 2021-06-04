import argparse
import sys
import glob
import os
import re
import pdb
import faulthandler

sys.path.append(os.path.join('scripts', 'devops_tasks'))
from common_tasks import get_package_properties

if __name__ == '__main__':
    faulthandler.enable()
    parser = argparse.ArgumentParser(description='Get package version details from the repo')
    parser.add_argument('-s', '--search_path', required=True, help='The scope of the search')
    args = parser.parse_args()

    seen_exception = 0
    pre_counter = 0
    counter = 0
    visible_setups = []
    expected_setups = []

    # prewalk to get number of setup.pys we actually expect to parse. this block will not be present in production code
    for root, dirs, files in os.walk(args.search_path):
        if re.search(r"sdk[\\/][^\\/]+[\\/][^\\/]+$", root):
            for filename in files:
                if os.path.basename(filename) == "setup.py":
                    pre_counter+=1
                    expected_setups.append(root + filename)

    print("I expect to see {} setup.pys parsed".format(pre_counter))
    


    for root, dirs, files in os.walk(args.search_path):
        if re.search(r"sdk[\\/][^\\/]+[\\/][^\\/]+$", root):
            for filename in files:
                if os.path.basename(filename) == "setup.py":
                    #if os.path.basename(root) != 'azure-mgmt' and os.path.basename(root) != 'azure' and os.path.basename(root) != 'azure-storage' and os.path.basename(root) != 'tests':
                    counter += 1
                    visible_setups.append(root + filename)
                    try:
                        # print("entering {}".format(root + filename))
                        pkgName, version, is_new_sdk, setup_py_path = get_package_properties(root)
                        # print("{0} {1} {2} {3}".format(pkgName, version, is_new_sdk, setup_py_path))
                    except RuntimeError as rte:
                        # Skip setup.py if the package cannot be parsed
                        # print("excepting against {}".format(filename))
                        # print("I have seen {} setup.pys so far".format(counter))
                        seen_exception = True
                        print("expected set")
                        print(expected_setups)
                        print("seen set")
                        print(visible_setups)


                if seen_exception:
                    print("I saw an exception and am continuing loop")
                    print()

            
                            
                        
                        