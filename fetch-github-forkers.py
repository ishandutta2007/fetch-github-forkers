import os
import requests

def get_forkers(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # Optional: Add token to avoid strict rate limits
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    forkers = []
    page = 1
    per_page = 100  # Max allowed per page
    
    while True:
        params = {"per_page": per_page, "page": page}
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.json().get('message')}")
            break
            
        data = response.json()
        if not data:
            break
            
        for fork in data:
            owner_info = fork.get("owner", {})
            forkers.append({
                "username": owner_info.get("login"),
                "html_url": owner_info.get("html_url"),
                "fork_repo_url": fork.get("html_url")
            })
            
        if len(data) < per_page:
            break
        page += 1
        
    return forkers

if __name__ == "__main__":
    owner_name = "SylphAI-Inc"
    repo_name = "skills"
    
    print(f"Fetching forkers for {owner_name}/{repo_name}...")
    result = get_forkers(owner_name, repo_name)
    
    print(f"Found {len(result)} forks:")
    for f in result:
        print(f"- {f['username']} ({f['html_url']})")
