"""
Initial logic regarding the gh-wrapper
"""

import os
import sys
from cli import create_parser
from api_client import APIClient

base_url = os.getenv("GITHUB_BASE_URL")
bearer_token = os.getenv("GITHUB_BEARER_TOKEN")

if not base_url or not bearer_token:
    print("Base URL or bearer token not set in environment variables")
    print("Please set them and try again")
    sys.exit(1)

if __name__ == "__main__":

    args = create_parser()

    client = APIClient(base_url=base_url, bearer_token=bearer_token)

    results = None

    match (getattr(args, "resource", None), getattr(args, "action", None)):
        case ("repo","list"):
            owner = getattr(args, "owner", None)
            name = getattr(args, "name", None)
            org = getattr(args, "org", None)
            all_flags = getattr(args, "all", False)
            contributors = getattr(args, "contributors", False)
            tags = getattr(args, "tags", False)
            teams = getattr(args, "teams", False)
            languages = getattr(args, "languages", False)

            if args.owner and not args.all and not args.name:
                raise ValueError("Repository name is required, please use --name")

            if args.owner and args.all:
                print(f"Getting all repositories from {args.owner}")
                results = client.get(f"/users/{args.owner}/repos")

            if args.owner and args.name:
                if args.contributors:
                    print(f"Getting repository contributors from {args.name}")
                    results = client.get(f"/repos/{args.owner}/{args.name}/contributors")
                elif args.owner and args.languages:
                    print(f"Getting all languages associated with the repository {args.name}")
                    results = client.get(f"/repos/{args.owner}/{args.name}/languages")
                elif args.owner and args.tags:
                    print(f"Getting all tags associated with the repository {args.name}")
                    results = client.get(f"/repos/{args.owner}/{args.name}/tags")
                elif args.owner and args.teams:
                    print(f"Getting all teams associated with the repository {args.name}")
                    results = client.get(f"/repos/{args.owner}/{args.name}/teams")
                else:
                    print(f"Getting repository {args.name} from {args.owner}")
                    results = client.get(f"/repos/{args.owner}/{args.name}")
            else:
                print("Missing arguments for repo list. See --help for usage.")
    print(results)
