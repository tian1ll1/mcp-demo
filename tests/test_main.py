"""
Test cases for GitHub operations
"""
import unittest
from unittest.mock import patch, MagicMock
from src.main import GitHubOperations

class TestGitHubOperations(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.github_ops = GitHubOperations(token="test-token")

    @patch('github.Github')
    def test_create_repository(self, mock_github):
        """Test repository creation."""
        # Mock setup
        mock_user = MagicMock()
        mock_repo = MagicMock()
        mock_repo.html_url = "https://github.com/test/test-repo"
        mock_repo.full_name = "test/test-repo"
        mock_user.create_repo.return_value = mock_repo
        mock_github.return_value.get_user.return_value = mock_user

        # Test
        result = self.github_ops.create_repository(
            name="test-repo",
            description="Test repository"
        )

        self.assertTrue(result['success'])
        self.assertEqual(result['repo_url'], "https://github.com/test/test-repo")
        self.assertEqual(result['repo_name'], "test/test-repo")

    @patch('github.Github')
    def test_create_issue(self, mock_github):
        """Test issue creation."""
        # Mock setup
        mock_repo = MagicMock()
        mock_issue = MagicMock()
        mock_issue.number = 1
        mock_issue.html_url = "https://github.com/test/test-repo/issues/1"
        mock_repo.create_issue.return_value = mock_issue
        mock_github.return_value.get_repo.return_value = mock_repo

        # Test
        result = self.github_ops.create_issue(
            repo_name="test/test-repo",
            title="Test Issue"
        )

        self.assertTrue(result['success'])
        self.assertEqual(result['issue_number'], 1)
        self.assertEqual(result['issue_url'], "https://github.com/test/test-repo/issues/1")

if __name__ == '__main__':
    unittest.main()