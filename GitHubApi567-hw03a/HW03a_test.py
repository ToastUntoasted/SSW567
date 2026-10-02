import unittest
from HW03a import get_repositories


class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        result = get_repositories("ToastUntoasted")

        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_known_repository(self):
        result = get_repositories("ToastUntoasted")

        repo_names = [repo[0] for repo in result]

        self.assertIn("SSW567", repo_names)

    def test_commit_counts(self):
        result = get_repositories("ToastUntoasted")

        for repo_name, commit_count in result:
            self.assertIsInstance(commit_count, int)
            self.assertGreaterEqual(commit_count, 0)

    def test_invalid_user(self):
        result = get_repositories(
            "this_user_should_not_exist_123456789"
        )

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()