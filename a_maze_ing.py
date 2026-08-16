#!/usr/bin/env python3
import sys

from src.mazegen.maze_config import MazeConfig
from src.mazegen.maze_generator import MazeGenerator

MAX_ARGS: int = 3


def main() -> None:
    if len(sys.argv) != MAX_ARGS:
        sys.exit(1)


if __name__ == "__main__":
    main()
