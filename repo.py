"""
Repository related functions
"""

from api_client import APIClient
from logger import get_logger


def repository(base_url, bearer_token, args):
    """
    Function to get repository data from GitHub
    """
    results = None

    client = APIClient(base_url=base_url, bearer_token=bearer_token)
    logger = get_logger(level=getattr(args, "log_level", "INFO"))

    match getattr(args, "action", None):
        case "list":
            owner = getattr(args, "owner", None)
            name = getattr(args, "name", None)
            all_flags = getattr(args, "all", False)
            contributors = getattr(args, "contributors", False)
            tags = getattr(args, "tags", False)
            teams = getattr(args, "teams", False)
            languages = getattr(args, "languages", False)
            org = getattr(args, "org", None)

            if org:
                logger.info("Getting all repositories from organization %s", org)
                results = client.get(f"/orgs/{org}/repos")

            if owner and not all_flags and not name:
                raise ValueError("Repository name is required, please use --name")

            if owner:
                if all_flags:
                    logger.info("Getting all repositories from %s", owner)
                    results = client.get(f"/users/{owner}/repos")
                if name:
                    if contributors:
                        logger.info("Getting repository contributors from %s", name)
                        results = client.get(f"/repos/{owner}/{name}/contributors")
                    elif owner and languages:
                        logger.info(
                            "Getting all languages associated with the repository %s",
                            name,
                        )
                        results = client.get(f"/repos/{owner}/{name}/languages")
                    elif owner and tags:
                        logger.info(
                            "Getting all tags associated with the repository %s", name
                        )
                        results = client.get(f"/repos/{owner}/{name}/tags")
                    elif owner and teams:
                        logger.info(
                            "Getting all teams associated with the repository %s", name
                        )
                        results = client.get(f"/repos/{owner}/{name}/teams")
                    else:
                        logger.info("Getting repository %s from %s", name, owner)
                        results = client.get(f"/repos/{owner}/{name}")
            return results
