# fetch-github-forkers

A lightweight, efficient command-line interface (CLI) tool designed to fetch all the forks of a given GitHub repository and append the list of forkers' usernames to a specified file. 

With automatic pagination handling, it seamlessly fetches information even for repositories with thousands of forks.

---

## 🚀 Features

* **CLI Driven**: Simple, intuitive command-line arguments.
* **Pagination Support**: Automatically handles GitHub API pagination, fetching 100 results per page to optimize API limits.
* **Detailed Logging**: Prints verbose pagination logs to keep you informed during large fetches.
* **Non-Destructive Output**: Appends results line-by-line to your target file instead of overwriting it.
* **Auth Support**: Can utilize a `GITHUB_TOKEN` to increase API rate limits.

---

## 📦 For Users: Installation & Usage

### Installation

You can install the package directly from PyPI:

```bash
pip install fetch-github-forkers
```

### Usage

Once installed, a global `fetch-github-forkers` executable is added to your system path.

**Syntax:**
```bash
fetch-github-forkers <owner> <repository> <output_file>
```

**Example:**
To fetch everyone who forked the repository `SylphAI-Inc/skills` and save them into `output.txt`:

```bash
fetch-github-forkers SylphAI-Inc skills output.txt
```

#### Bypassing Rate Limits
GitHub limits unauthenticated API requests. If you are fetching forks for a massive repository, you might hit this limit. To increase your limit, generate a [GitHub Personal Access Token](https://github.com/settings/tokens) and expose it as an environment variable before running the tool:

**On Linux/macOS:**
```bash
export GITHUB_TOKEN="your_personal_access_token"
fetch-github-forkers SylphAI-Inc skills output.txt
```

**On Windows (PowerShell):**
```powershell
$env:GITHUB_TOKEN="your_personal_access_token"
fetch-github-forkers SylphAI-Inc skills output.txt
```

---

## 💻 For Developers: Local Development

If you want to contribute, modify the code, or build it locally, follow these steps.

### Setup Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fetch-github-forkers.git
   cd fetch-github-forkers
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the package in editable mode:**
   This allows you to edit `fetch_github_forkers.py` and see the changes reflected immediately when you run the CLI command without reinstalling.
   ```bash
   pip install -e .
   ```

### Code Structure
* `fetch_github_forkers.py`: The core script containing the GitHub API interactions and the CLI `argparse` configuration.
* `setup.py`: The package metadata file used to configure PyPI builds and entry points.
* `.github/workflows/publish.yml`: The GitHub Actions pipeline for CI/CD.

---

## 🚀 For Package Publishers: Release Guide

This project is configured with a **Continuous Deployment (CD) pipeline via GitHub Actions**. 

Whenever a change to `setup.py` is pushed to the `main` (or `master`) branch, the pipeline will automatically build the distribution wheels and attempt to upload them to PyPI.

### Initial Setup (One-time only)
To allow GitHub Actions to publish on your behalf:
1. Log into [PyPI](https://pypi.org/manage/account/) and generate an API Token.
2. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
3. Create a new repository secret named `PYPI_API_TOKEN` and paste your PyPI token.

### Releasing a New Version
1. Open `setup.py` and increment the `version` string (e.g., from `"0.1.0"` to `"0.1.1"`). Follow [Semantic Versioning](https://semver.org/).
2. Stage and commit your changes:
   ```bash
   git add setup.py
   git commit -m "Bump version to 0.1.1"
   ```
3. Push to the main branch:
   ```bash
   git push origin main
   ```
4. The GitHub Action will trigger automatically. You can watch the build and upload progress in the **Actions** tab of your repository. 

*(Note: The pipeline uses `--skip-existing`. If you push changes to `setup.py` without bumping the version number, the workflow will succeed but will safely skip the PyPI upload).*
