from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mazegen.maze_config import MazeConfig


class MazeGenerator:
    def __init__(self, config: MazeConfig) -> None:
        self.config = config
        self.width = config.width
        self.height = config.height
        self.grid: list[list[int]] = []

        self.create_grid()

    def create_grid(self) -> None:
        for _i in range(self.height):
            row: list = [0b1111 for _ in range(self.width)]
            self.grid.append(row)
