import unittest
from unittest.mock import patch, Mock

from HW03a import get_repositories


class TestGitHubAPI(unittest.TestCase):

    @patch("HW03a.requests.get")
    def test_valid_user(self, mock_get):

        repo_response = Mock()
        repo_response.status_code = 200
        repo_response.json.return_value = [
            {
                "name": "Repo1",
                "commits_url":
                    "https://api.github.com/repos/testuser/Repo1/commits{/sha}"
            },
            {
                "name": "Repo2",
                "commits_url":
                    "https://api.github.com/repos/testuser/Repo2/commits{/sha}"
            }
        ]

        repo1_commits = Mock()
        repo1_commits.status_code = 200
        repo1_commits.json.return_value = [
            {"sha": "1"},
            {"sha": "2"}
        ]

        repo2_commits = Mock()
        repo2_commits.status_code = 200
        repo2_commits.json.return_value = [
            {"sha": "1"},
            {"sha": "2"},
            {"sha": "3"}
        ]

        mock_get.side_effect = [
            repo_response,
            repo1_commits,
            repo2_commits
        ]

        result = get_repositories("testuser")

        self.assertEqual(
            result,
            [
                ("Repo1", 2),
                ("Repo2", 3)
            ]
        )


    @patch("HW03a.requests.get")
    def test_invalid_user(self, mock_get):

        response = Mock()
        response.status_code = 404
        response.json.return_value = {
            "message": "Not Found"
        }

        mock_get.return_value = response

        result = get_repositories("baduser")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()