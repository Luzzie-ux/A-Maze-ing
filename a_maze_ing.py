#!/usr/bin/env python3
import sys
from pathlib import Path
from platform import python_version

from pydantic import ValidationError

from parsing_utils import checker
from src.mazegen.maze_config import MazeConfig
from src.mazegen.maze_generator import MazeGenerator

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
        fnf: str = "File Not Found"
        raise FileNotFoundError(fnf)

    raw: dict[str, str] = {}

    contents = file.read_text(encoding="utf-8")
    for content in contents.split("\n"):
        if content.startswith("#"):
            continue
        if "=" not in content:
            serr: str = "Invalid Syntax"
            raise SyntaxError(serr)

        key, value = content.split("=", 1)
        key = key.strip().upper()
        value = value.strip()
        raw[key] = value
    for key in KEYS:
        if key not in raw:
            missing: str = f"Missing: {key}"
            raise ValueError(missing)

    config: dict = {}
    for k, v in raw.items():
        try:
            f = checker[k]
            config[k.lower()] = f(v)
        except ValueError as e:
            raise ValueError(str(e)) from e
    return MazeConfig(**config)


def main() -> None:
    if len(sys.argv) != MAX_ARGS:
        sys.stderr.write(f"Usage: {python_version()} \n")
        sys.exit(1)
    try:
        config = parser(sys.argv[1])
        maze = MazeGenerator(config)
        print(maze.grid)
    except (FileNotFoundError, SyntaxError, ValueError) as e:
        sys.stderr.write(f"{e.__class__.__name__}: {e}\n")
        sys.exit(1)
    except ValidationError as err:
        sys.stderr.write(f"{err}\n")


if __name__ == "__main__":
    main()
