import argparse
from types import SimpleNamespace

from ci_tools.logging import initialize_logger

def clean_environment() -> None:
    parser = argparse.ArgumentParser(
        description="""This is the primary entrypoint for """,
    )

    parser.add_argument(
        "package",
        required=True,
        help=("Target path to generate a scenario against."),
    )

    parser.add_argument(
        "scenario",
        required=True,
        choices=["optional_inclusive", "optional_exclusive"],
        help=("The name of the scenario that should be generated for the targeted package."),
    )

    logger = initialize_logger('clean_environment')

    args, unknown = parser.parse_known_args()

    if args.scenario == "optional_inclusive":
        pass
    elif args.scenario == "optional_exclusive":
        pass
    else:
        print("Unrecognized error.")
        exit(1)