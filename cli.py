"""
File responsible to handle parsers
used by the application
"""

import argparse

def create_parser():
    """
    Build and parse arguments to CLI
    """
    parser = argparse.ArgumentParser(
        description="Arguments are needed to call functions",
        prog="gh-wrapper"
    )

    subparsers = parser.add_subparsers(dest="resource", required=False)

    repo_parser = subparsers.add_parser("repo", help="Repository operations")
    repo_subparsers = repo_parser.add_subparsers(dest="action", required=True)

    ## List Repository Arguments
    list_parser = repo_subparsers.add_parser("list", help="List repositories")
    list_parser.add_argument("--owner", required=False, help="Repository owner")
    list_parser.add_argument(
        "--name",
        required=False,
        help="Reposiroty name"
        )
    list_parser.add_argument(
        "--org",
        required=False,
        action="store_true",
        help="Organization name"
        )
    list_parser.add_argument(
        "--all",
        required=False,
        action="store_true",
        help="Listing all records"
    )
    list_parser.add_argument(
        "--contributors",
        required=False,
        action="store_true",
        help="Listing repository contributors"
    )
    list_parser.add_argument(
        "--languages",
        required=False,
        action="store_true",
        help="Showing repository languages"
    )
    list_parser.add_argument(
        "--tags",
        required=False,
        action="store_true",
        help="Display repository tags"
    )
    list_parser.add_argument(
        "--teams",
        required=False,
        action="store_true",
        help="Display repository teams"
    )

    return parser.parse_args()
