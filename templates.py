import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',)

def create_files_and_directories(list_of_files):
    """
    Creates files and directories from a given list of file paths.

    Args:
        list_of_files (list): A list of file paths to be created.

    Returns:
        None

    Example:
        >>> list_of_files = [
       ...     "src/__init__.py",
       ...     "src/helper.py",
       ...     "src/prompt.py",
       ...     ".env",
       ...     "setup.py",
       ...     "Experiments/trails.ipynb",
       ...     "app.py",
       ...     "store_index.py",
       ...     "static/.gitkeep",
       ...     "template/index.html",
       ...     "static/style.css",
       ...     "template/script.js"
       ... ]
        >>> create_files_and_directories(list_of_files)
    """
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir!= "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass
            logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{filename} is already created")

# Example usage
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "Experiments/trails.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "template/index.html",
    "static/style.css",
    "template/script.js"
]
create_files_and_directories(list_of_files)