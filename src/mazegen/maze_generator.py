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
        ex, ey = self.config.entry
        sx, sy = self.config.exit
        for i in range(self.height):
            row: list = []
            for j in range(self.width):
                if i == ey and j == ex:
                    row.append(0b0000)
                    continue
                if i == sy and j == sx:
                    row.append(0b0000)
                    continue
                row.append(0b1111)
            self.grid.append(row)
