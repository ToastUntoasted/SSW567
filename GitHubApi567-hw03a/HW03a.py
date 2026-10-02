"""
Name: Robert Galletta
File: HW03a.py
Date: 1 October 2026
Description: You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.
"""
import requests


def get_repositories(user_id):
    response = requests.get(
        f"https://api.github.com/users/{user_id}/repos"
    )
    data = response.json()

    if not isinstance(data, list):
        return []

    results = []

    for item in data:
        repo_name = item["name"]

        response = requests.get(
            item["commits_url"].replace("{/sha}", "")
        )
        commits = response.json()

        results.append((repo_name, len(commits)))

    return results


if __name__ == "__main__":
    user_ID = input("Enter a GitHub user ID: ")

    repositories = get_repositories(user_ID)

    for repo, commits in repositories:
        print(f"Repo: {repo} Number of commits: {commits}")