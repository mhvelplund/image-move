import sys
from pathlib import Path
from shutil import copy, move


def move_images(
    source_path: Path,
    destination_path: Path,
    copy_file: bool,
    prefix: str,
    verbose: bool,
):
    source_files = [f for f in source_path.iterdir() if f.is_file()]

    index = 0
    for source_file in source_files:
        cmd = copy if copy_file else move
        new_name = f"{prefix}_{index}{source_file.suffix}"
        index += 1
        destination_file = Path(destination_path, new_name)
        if verbose:
            print(
                f"{'copy' if copy_file else 'move'} {source_file} -> {destination_file}",
                file=sys.stderr,
            )

        cmd(source_file, destination_file)
