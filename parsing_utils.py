from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def check_width(width: str) -> int:
    try:
        w = int(width)
    except ValueError as e:
        raise ValueError(str(e)) from e
    if w <= 0:
        zero: str = "WIDTH must be > than 0"
        raise ValueError(zero)
    return w


def check_height(height: str) -> int:
    try:
        h = int(height)
    except ValueError as e:
        raise ValueError(str(e)) from e
    if h <= 0:
        zero: str = "HEIGHT must be > than 0"
        raise ValueError(zero)
    return h


def check_entry(entry_point: str) -> tuple[int, int]:
    err: str
    if "," not in entry_point:
        err = "Entry must be in format x,y"
        raise ValueError(err)
    x, y = entry_point.split(",")
    try:
        entry: tuple[int, int] = (int(x), int(y))
    except ValueError as e:
        err = f"ENTRY must be an integer, got: {entry_point}"
        raise ValueError(err) from e
    if entry[0] < 0 or entry[1] < 0:
        out_of_bounds: str = "Entry out of bounds"
        raise ValueError(out_of_bounds)
    return entry


def check_exit(exit_point: str) -> tuple[int, int]:
    err: str
    if "," not in exit_point:
        err = "EXIT must be in format x,y"
        raise ValueError(err)
    x, y = exit_point.split(",")
    try:
        out: tuple[int, int] = (int(x), int(y))
    except ValueError as e:
        err = f"EXIT must be an integer, got: {exit_point}"
        raise ValueError(err) from e
    if out[0] < 0 or out[1] < 0:
        out_of_bounds: str = "EXIT out of bounds"
        raise ValueError(out_of_bounds)
    return out


def check_file(file: str) -> str:
    if Path(file).exists():
        return file
    return file


def check_perfect(perfect: str) -> bool:
    if perfect in {"True", "TRUE"}:
        return True
    if perfect in {"False", "FALSE"}:
        return False
    staterr: str = f"PERFECT must be True or False, got: {perfect}"
    raise ValueError(staterr)


def check_seed(seed: str) -> int:
    try:
        sed = int(seed)
    except ValueError as e:
        raise ValueError(str(e)) from e
    if sed <= 0:
        zero: str = "SEED must be > than 0"
        raise ValueError(zero)
    return sed


def check_algo(algo: str) -> str:
    if algo == " ":
        return "bfs"
    return algo


def check_display(display: str) -> str:
    return display


checker: dict[str, Callable] = {
    "WIDTH": check_width,
    "HEIGHT": check_height,
    "ENTRY": check_entry,
    "EXIT": check_exit,
    "OUTPUT_FILE": check_file,
    "PERFECT": check_perfect,
    "SEED": check_seed,
    "ALGORITHM": check_algo,
    "DISPLAY": check_display,
}
