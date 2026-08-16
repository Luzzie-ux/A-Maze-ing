from dataclasses import dataclass


@dataclass
class MazeConfig:
    width: int
    height: int
    entry_point: tuple[int, int]
    exit_point: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None
    algorithm: str | None
    display: str | None
