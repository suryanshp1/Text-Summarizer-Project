import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Union


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_create: list, verbose=False):
    """
    Creates a list of directories if they don't exist.

    Args:
        path_to_create (list): A list of directories to create.
        verbose (bool, optional): If True, print information about the operation. Defaults to False.
    """
    for path in path_to_create:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> Union[float, int]:
    """
    Calculates the size of a file in bytes.

    Args:
        path (Path): The path to the file.

    Returns:
        float: The size of the file in bytes.
    """
    if not os.path.exists(path):
        return 0
    return os.path.getsize(path)