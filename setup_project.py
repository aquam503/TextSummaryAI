import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define your project name
project_name = "SummarizeAI"  # Project name

# List of files to create
files_to_create = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    ".gitignore"
]

# Create directories and files
for file_path in files_to_create:
    path = Path(file_path)
    directory, filename = os.path.split(path)

    # Create directories if they don't exist
    if directory:
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Created directory: {directory}")

    # Create file if it doesn't exist or is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()  # Create empty file
        logging.info(f"Created file: {path}")
    else:
        logging.info(f"File already exists: {path}")