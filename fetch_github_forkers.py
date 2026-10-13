import os
import requests
import argparse

def get_forkers(owner, repo, output_file):
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
    
    print(f"Fetching forkers for {owner}/{repo}...")
    
    while True:
        params = {"per_page": per_page, "page": page}
        print(f"Fetching page {page} (up to {per_page} items)...")
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.json().get('message')}")
            break
            
        data = response.json()
        if not data:
            print(f"No forks found on page {page}.")
            break
            
        print(f"Retrieved {len(data)} forks from page {page}.")
        for fork in data:
            owner_info = fork.get("owner", {})
            username = owner_info.get("login")
            if username:
                forkers.append(username)
            
        if len(data) < per_page:
            break
        page += 1
        
    if forkers:
        print(f"Total {len(forkers)} forks fetched. Appending to {output_file}...")
        with open(output_file, "a", encoding="utf-8") as f:
            for username in forkers:
                f.write(f"- {username}\n")
        print("Done appending.")
    else:
        print("No forks found to append.")
        
    return forkers

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub forkers and append them to a file.")
    parser.add_argument("owner", help="GitHub username or organization (owner of the repository)")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("output_file", help="File to append the list of forkers")
    
    args = parser.parse_args()
    
    get_forkers(args.owner, args.repo, args.output_file)

if __name__ == "__main__":
    main()
