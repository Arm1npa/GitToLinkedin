import requests
import base64


def get_github_repo_info(repo_url):
    """Fetch repo name, description, README, languages, and topics from GitHub API."""
    try:
        # Extract owner/repo from URL
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {"Accept": "application/vnd.github+json"}
        repo_resp = requests.get(api_url, headers=headers)
        if repo_resp.status_code != 200:
            return None
        repo_data = repo_resp.json()
        # Get README
        readme_resp = requests.get(f"{api_url}/readme", headers=headers)
        readme = ""
        if readme_resp.status_code == 200:
            readme_json = readme_resp.json()
            readme = base64.b64decode(readme_json.get(
                'content', '')).decode('utf-8', errors='ignore')
        # Get languages
        lang_resp = requests.get(f"{api_url}/languages", headers=headers)
        languages = list(lang_resp.json().keys()
                         ) if lang_resp.status_code == 200 else []
        # Get topics
        topics_resp = requests.get(
            f"{api_url}/topics", headers={**headers, "Accept": "application/vnd.github.mercy-preview+json"})
        topics = topics_resp.json().get(
            'names', []) if topics_resp.status_code == 200 else []
        return {
            "name": repo_data.get('name', ''),
            "description": repo_data.get('description', ''),
            "readme": readme,
            "languages": languages,
            "topics": topics,
            "html_url": repo_data.get('html_url', repo_url)
        }
    except Exception as e:
        return None
