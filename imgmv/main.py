import argparse
import sys
from pathlib import Path

from .imgmv import move_images


def run():
    parser = argparse.ArgumentParser(
        prog="imgmv",
        description="Rename images based on their folder.",
    )
    parser.add_argument(
        "source",
        type=str,
        help="the source folder containing the images",
    )
    parser.add_argument(
        "destination",
        type=str,
        help='the target folder to put the renamed images. Defaults to "."',
        nargs="?",
        default=".",
    )
    parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        help="copy instead of moving",
    )
    parser.add_argument(
        "-V",
        "--verbose",
        action="store_true",
        help="log file actions",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        type=str,
        help="the image prefix to use. Defaults to the source folder name",
    )
    args = parser.parse_args()

    source_path = Path(args.source).resolve()

    if not source_path.exists():
        print(
            f'Source folder "{source_path}" does not exist.',
            file=sys.stderr,
        )
        exit(1)

    if not source_path.is_dir():
        print(
            f'Source "{source_path}" is not a folder.',
            file=sys.stderr,
        )
        exit(1)

    destination_path = Path(args.destination).resolve()

    if not destination_path.exists():
        print(
            f'Destination folder "{destination_path}" does not exist.',
            file=sys.stderr,
        )
        exit(1)

    if not destination_path.is_dir():
        print(
            f'Destination "{destination_path}" is not a folder.',
            file=sys.stderr,
        )
        exit(1)

    copy = args.copy
    prefix = args.prefix or source_path.name
    verbose = args.verbose

    move_images(source_path, destination_path, copy, prefix, verbose)
