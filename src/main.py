"""
MCP Demo - GitHub Operations Example
"""
import os
from github import Github

class GitHubOperations:
    def __init__(self, token=None):
        """Initialize GitHub client with token."""
        self.token = token or os.getenv('GITHUB_TOKEN')
        if not self.token:
            raise ValueError("GitHub token is required")
        self.client = Github(self.token)

    def create_repository(self, name, description=None, private=False):
        """Create a new repository."""
        try:
            repo = self.client.get_user().create_repo(
                name=name,
                description=description,
                private=private
            )
            return {
                'success': True,
                'repo_url': repo.html_url,
                'repo_name': repo.full_name
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def create_issue(self, repo_name, title, body=None):
        """Create a new issue in the specified repository."""
        try:
            repo = self.client.get_repo(repo_name)
            issue = repo.create_issue(title=title, body=body)
            return {
                'success': True,
                'issue_number': issue.number,
                'issue_url': issue.html_url
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def create_pull_request(self, repo_name, title, head, base='main', body=None):
        """Create a new pull request."""
        try:
            repo = self.client.get_repo(repo_name)
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head,
                base=base
            )
            return {
                'success': True,
                'pr_number': pr.number,
                'pr_url': pr.html_url
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

if __name__ == '__main__':
    # Example usage
    github_ops = GitHubOperations()
    result = github_ops.create_repository(
        name="test-repo",
        description="A test repository"
    )
    print(result)