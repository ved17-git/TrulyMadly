import requests
import os
from dotenv import load_dotenv
load_dotenv()


def github_repo_search(query: str):

    url = "https://api.github.com/search/repositories"

    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"
    }

    params = {"q": query, "sort": "stars", "order": "desc"}

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    top_repos = []

    for repo in data["items"][:3]:
        top_repos.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        })

    return top_repos
