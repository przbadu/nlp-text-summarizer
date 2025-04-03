import os
import yaml

from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
  """reads yaml file and returns

  Args:
    path (str): path to yaml file

  Raises:
    valueError: if yaml file is empty
    e: empty file

  Returns:
    ConfigBox: ConfigBox type
  """
  try:
    with open(path) as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f"yaml file: {path} loaded successfully")
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
    raise e


@ensure_annotations
def create_directories(paths: list, verbose=True):
  """Create list of directories

  Args:
    path (list): list of directories path
    ignore_log (bool, optional): ignore if multiple dirs needs to be created. Defaults to False.
  """

  for path in paths:
    os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
  """get size in KB

  Args:
    path (Path): path of the file

  Returns:
    str: size in KB
  """

  size_in_kb = round(os.path.getsize(path)/1024)
  return f"~ {size_in_kb} KB"

