import argparse
from types import SimpleNamespace

from ci_tools.logging import initialize_logger

def align_environment() -> None:
    parser = argparse.ArgumentParser(
        description="""This is the primary entrypoint for the "build" action. This command is used to build any package within the azure-sdk-for-python repository.""",
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

    logger = initialize_logger('generator')

    args, unknown = parser.parse_known_args()

    if args.scenario == "optional_inclusive":
        pass
    elif args.scenario == "optional_exclusive":
        pass
    else:
        print("Unrecognized error.")
        exit(1)

def optional_scenario(package: str, additional_args: SimpleNamespace, inclusive=True) -> None:
    """
    Used to generate an 'optional' scenario. This effectively means installing a package, its dev_reqs, and any necessary common tooling,
    then explicitly _removing_ some optional packages from the environment before testing.
    """


