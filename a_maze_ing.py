#!/usr/bin/env python3
import sys
from pathlib import Path
from platform import python_version

from src.mazegen.maze_config import MazeConfig
from src.mazegen.maze_generator import MazeGenerator

from .parsing_utils import switch

MAX_ARGS: int = 2
KEYS: list[str] = [
    "WIDTH",
    "HEIGHT",
    "ENTRY",
    "EXIT",
    "OUTPUT_FILE",
    "PERFECT",
]


def parser(filename: str) -> MazeConfig:
    file = Path(filename)
    if not file.exists():
        raise FileNotFoundError

    raw: dict[str, str] = {}

    contents = file.read_text(encoding="utf-8")
    for content in contents.split("\n"):
        if content.startswith("#"):
            continue
        if "=" not in content:
            raise SyntaxError

        key, value = content.split("=", 1)
        key = key.strip().upper()
        value = value.strip()
        raw[key] = value

    for v in raw.values():
        try:
            config = switch(v)
        except ValueError as e:
            raise ValueError from e

    return MazeConfig(*config)


def main() -> None:
    if len(sys.argv) != MAX_ARGS:
        sys.stderr.write(f"Usage: {python_version()} \n")
        sys.exit(1)
    try:
        parser(sys.argv[1])
    except (FileNotFoundError, SyntaxError, ValueError) as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
