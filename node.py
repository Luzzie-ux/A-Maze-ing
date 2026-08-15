class Node:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._locked: bool = True

    def get_name(self) -> str:
        return self._name

    def get_state(self) -> bool:
        return self._locked

    def set_state(self) -> None:
        if not self._locked:
            self._locked = True