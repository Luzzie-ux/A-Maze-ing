from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def check_width(width: str) -> int: ...


def check_height(height: str) -> int: ...


def check_entry(entry: str) -> tuple[int, int]: ...


def check_exit(exit: str) -> tuple[int, int]: ...


def check_file(file: str) -> str: ...


def check_perfect(perfect: str) -> bool: ...


def check_seed(sedd: str) -> int: ...


def check_algo(algo: str) -> str: ...


def check_display(display: str) -> str: ...


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


def switch(value: str) -> list:
    try:
        config: list = [f(value) for f in checker.values()]
    except ValueError as e:
        raise ValueError from e
    return config
