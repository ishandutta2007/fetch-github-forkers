from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fetch-github-forkers",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to fetch GitHub forkers and append them to a file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fetch-github-forkers",
    py_modules=["fetch_github_forkers"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "fetch-github-forkers=fetch_github_forkers:main",
        ],
    },
)
