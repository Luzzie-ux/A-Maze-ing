from typing import Self

from pydantic import BaseModel, Field, model_validator


class MazeConfig(BaseModel):
    width: int = Field(gt=0, le=100)
    height: int = Field(gt=0, le=100)
    entry: tuple[int, int] = Field(min_length=2, max_length=2)
    exit: tuple[int, int] = Field(min_length=2, max_length=2)
    output_file: str = Field(default="maze.txt")
    perfect: bool = Field(default=False)
    seed: int | None = Field(default=42)
    algorithm: str | None = Field(default="bfs")
    display: str | None = Field(default="mlx")

    @model_validator(mode="after")
    def validate(self) -> Self:
        ex, ey = self.entry
        enerr: str = f"Exit ({ex}, {ey}) must be smaller than "
        if ex > self.width:
            werr = f"{enerr} width: ({self.width})!"
            raise ValueError(werr)
        if ey > self.height:
            herr = f"{enerr} height: ({self.height})!"
            raise ValueError(herr)
        sx, sy = self.exit
        exerr: str = f"Exit ({sx}, {sy}) must be smaller than "
        if sx > self.width:
            werr = f"{exerr} width: ({self.width})!"
            raise ValueError(werr)
        if sy > self.height:
            herr = f"{exerr} height: ({self.height})!"
            raise ValueError(herr)
        return self
