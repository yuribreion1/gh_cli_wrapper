"""
Repository related functions
"""

from api_client import APIClient


def repository(base_url, bearer_token, args):
    """
    Function to get repository data from GitHub
    """
    results = None

    client = APIClient(base_url=base_url, bearer_token=bearer_token)

    match getattr(args, "action", None):
        case "list":
            owner = getattr(args, "owner", None)
            name = getattr(args, "name", None)
            all_flags = getattr(args, "all", False)
            contributors = getattr(args, "contributors", False)
            tags = getattr(args, "tags", False)
            teams = getattr(args, "teams", False)
            languages = getattr(args, "languages", False)

            if owner and not all_flags and not name:
                raise ValueError("Repository name is required, please use --name")

            if owner:
                if all_flags:
                    print(f"Getting all repositories from {owner}")
                    results = client.get(f"/users/{owner}/repos")
                if name:
                    if contributors:
                        print(f"Getting repository contributors from {name}")
                        results = client.get(f"/repos/{owner}/{name}/contributors")
                    elif owner and languages:
                        print(
                            f"Getting all languages associated with the repository {name}"
                        )
                        results = client.get(f"/repos/{owner}/{name}/languages")
                    elif owner and tags:
                        print(f"Getting all tags associated with the repository {name}")
                        results = client.get(f"/repos/{owner}/{name}/tags")
                    elif owner and teams:
                        print(
                            f"Getting all teams associated with the repository {name}"
                        )
                        results = client.get(f"/repos/{owner}/{name}/teams")
                    else:
                        print(f"Getting repository {name} from {owner}")
                        results = client.get(f"/repos/{owner}/{name}")
                else:
                    print("Missing arguments for repo list. See --help for usage.")
            return results
