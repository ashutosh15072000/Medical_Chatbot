import os 
from box.exceptions import BoxValueError
import yaml
from src.logger import logging_config
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Dict, Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

   
    # :Reads a YAML file and returns a ConfigBox object. 

    # Args:
    #     path_to_yaml (Path): The path to the YAML file to read.

    # Returns:
    #     ConfigBox: A ConfigBox object containing the YAML file's content.

    # Raises:
    #     Exception: If the file is not found, permission is denied, or there's an error parsing the YAML file.

    # Example:
    #     >>> from pathlib import Path
    #     >>> yaml_file_path = Path('example.yaml')
    #     >>> config_box = read_yaml(yaml_file_path)
    #     >>> print(config_box)  # prints the content of the YAML file as a ConfigBox object
   


    
    
    try:
        with open(path_to_yaml) as yaml_file:
            content: Dict[str, Any] = yaml.safe_load(yaml_file)
            logging_config.configure_logging(f"Yaml File: {path_to_yaml} Loaded Successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        raise Exception(f"File not found: {path_to_yaml}")
    except PermissionError:
        raise Exception(f"Permission denied: {path_to_yaml}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")
    except Exception as e:
        raise Exception(f"Error occurred while reading yaml file: {e}") from e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories at the specified paths.

    Args:
        path_to_directories (list): A list of paths where directories need to be created.
        verbose (bool, optional): If True, logs a message for each directory created. Defaults to True.

    Example:
        >>> create_directories(["/path/to/directory1", "/path/to/directory2"])
        Created Directory at: /path/to/directory1
        Created Directory at: /path/to/directory2

    Notes:
        This function uses `os.makedirs` with `exist_ok=True` to avoid raising an error if the directory already exists.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging_config.configure_logging(f"Created Directory at: {path}")