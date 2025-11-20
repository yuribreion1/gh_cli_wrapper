"""
Initial logic regarding the gh-wrapper
"""

import os
import sys
from cli import create_parser
from repo import repository

base_url = os.getenv("GITHUB_BASE_URL")
bearer_token = os.getenv("GITHUB_BEARER_TOKEN")

if not base_url or not bearer_token:
    print("Base URL or bearer token not set in environment variables")
    print("Please set them and try again")
    sys.exit(1)

if __name__ == "__main__":

    args = create_parser()

    match getattr(args, "resource", None):
        case ("repo"):
            data = repository(base_url=base_url, bearer_token=bearer_token, args=args)
