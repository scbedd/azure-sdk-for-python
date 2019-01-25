
#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Below are common methods for the devops build steps. This is the common location that will be updated with 
# package targeting during release.

import glob
from pathlib import Path, PurePath
from subprocess import check_output, CalledProcessError
import os
import fnmatch

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..'))

def get_updated_package_list():
    try:
        updated_files = check_output(['git','diff','master','--name-only'], shell=True).splitlines()
        
        paths = [os.path.join(i.decode()) for i in updated_files]
        
        for path in paths:
            basename = None
            rel_path = path

            while rel_path:
                rel_path, basename = os.path.split(rel_path)

        # get path object for easy manipulation
        top_level_directories = [PurePath(i) for i in paths]
        
        # get left most directory or file
        top_level_directories = [p.parts[0] for p in top_level_directories]

        # de-duplicate
        top_level_directories = list(set(top_level_directories))

        # check against package format
        top_level_directories = fnmatch.filter(top_level_directories, 'azure-*')

        return top_level_directories
    except CalledProcessError as err:
        print(err) #, file = sys.stderr
        sys.exit(1)

if __name__ == '__main__':
    print(get_updated_package_list())