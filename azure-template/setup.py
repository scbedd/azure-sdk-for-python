from setuptools import setup, find_packages
import os
from io import open
import re

PACKAGE_NAME = "azure-template"
PACKAGE_PPRINT_NAME = "Template Package"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace('-', '/')
# a-b-c => a.b.c
namespace_name = PACKAGE_NAME.replace('-', '.')

# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, 'version.py'), 'r') as fd:
    version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    version=version,
    description='Microsoft Azure {} Client Library for Python'.format(PACKAGE_PPRINT_NAME),
    long_description=long_description,
    url='https://github.com/Azure/azure-sdk-for-python',
    author='Microsoft Corporation',
    author_email='azuresdkengsysadmins@microsoft.com',
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=[
        'tests',
        # Exclude packages that will be covered by PEP420 or nspkg
        'azure'
    ]),
    install_requires=[
        'peppercorn'
        #,'msrest>=0.5.0'
        #,'azure-common~=1.1'
    ],
    extras_require={
        ":python_version<'3.0'": ['azure-nspkg'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Azure/azure-sdk-for-python/issues',
        'Source': 'https://github.com/Azure/azure-sdk-python',
    }
)
