from pathlib import Path
from shutil import copy, move
from typing import Tuple


def move_images(
  source_path: Path,
  destination_path: Path,
  copy_file: bool,
  prefix: str,
  verbose: bool = False,
  dry_run: bool = False,
):
  source_files = [f for f in source_path.iterdir() if f.is_file()]

  def nop(*args, **kwargs):
    pass

  cmd = nop if dry_run else copy if copy_file else move
  cmd_name = "copy" if copy_file else "move"

  for source_file, destination_file in generate_source_destination_pairs(source_files, destination_path, prefix):
    if verbose:
      print(f"{cmd_name} {source_file} -> {destination_file}")
    cmd(source_file, destination_file)


def generate_source_destination_pairs(
  source_files: list[Path], destination_path: Path, prefix: str
) -> list[Tuple[Path, Path]]:
  """
  Generate a list of source and destination file path pairs.
  This function takes a list of source file paths, a destination directory path,
  and a prefix string. It generates destination file paths by appending the prefix
  and an index to the original file name, preserving the original file extension.
  Args:
    source_files (list[Path]): A list of source file paths.
    destination_path (Path): The destination directory path.
    prefix (str): The prefix to be added to the destination file names.
  Returns:
    list[Tuple[Path, Path]]: A list of tuples, each containing a source file path
    and the corresponding destination file path.
  """

  def generate_destination_file(destination_path: Path, prefix: str, index: int, source_file: Path) -> Path:
    return Path(destination_path, f"{prefix}_{index}{source_file.suffix}")

  return [
    (source_file, generate_destination_file(destination_path, prefix, index, source_file))
    for index, source_file in enumerate(source_files)
  ]
