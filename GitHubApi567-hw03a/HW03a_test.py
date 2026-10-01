import unittest
from unittest.mock import patch, Mock

from HW03a import get_repositories


class TestGitHubAPI(unittest.TestCase):

    @patch("HW03a.requests.get")
    def test_one_repository(self, mock_get):

        repo_response = Mock()
        repo_response.json.return_value = [
            {
                "name": "TestRepo",
                "commits_url":
                    "https://api.github.com/repos/test/TestRepo/commits{/sha}"
            }
        ]

        commit_response = Mock()
        commit_response.json.return_value = [
            {"sha": "1"},
            {"sha": "2"},
            {"sha": "3"}
        ]

        mock_get.side_effect = [
            repo_response,
            commit_response
        ]

        result = get_repositories("test")

        self.assertEqual(
            result,
            [("TestRepo", 3)]
        )

    @patch("HW03a.requests.get")

    def test_multiple_repositories(self, mock_get):
        repo_response = Mock()
        repo_response.json.return_value = [
            {
                "name": "Repo1",
                "commits_url":
                    "https://api.github.com/repos/test/Repo1/commits{/sha}"
            },
            {
                "name": "Repo2",
                "commits_url":
                    "https://api.github.com/repos/test/Repo2/commits{/sha}"
            }
        ]

        repo1_commits = Mock()
        repo1_commits.json.return_value = [
            {"sha": "1"},
            {"sha": "2"}
        ]

        repo2_commits = Mock()
        repo2_commits.json.return_value = [
            {"sha": "1"},
            {"sha": "2"},
            {"sha": "3"},
            {"sha": "4"}
        ]

        mock_get.side_effect = [
            repo_response,
            repo1_commits,
            repo2_commits
        ]

        result = get_repositories("test")

        self.assertEqual(
            result,
            [
                ("Repo1", 2),
                ("Repo2", 4)
            ]
        )
        
    @patch("HW03a.requests.get")
    def test_no_repositories(self, mock_get):

        repo_response = Mock()
        repo_response.json.return_value = []

        mock_get.return_value = repo_response

        result = get_repositories("test")

        self.assertEqual(result, [])
    


if __name__ == "__main__":
    unittest.main()