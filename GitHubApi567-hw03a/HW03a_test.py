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

    def test_invalid_user(self):
        result = get_repositories("this_user_should_not_exist_123456789")

        self.assertEqual(result, [{"message": "Not Found", "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user", "status": 404}])


if __name__ == "__main__":
    unittest.main()