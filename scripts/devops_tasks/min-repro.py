from common_tasks import parse_setup

import os

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))
target_package_for_parsing = os.path.join(root_dir, "sdk", "identity", "azure-identity")
reqs = parse_setup(target_package_for_parsing)

print(reqs)
