from node import Node


class Graph:
    def __init__(self) -> None:
        self._nodes: list[Node] = []

    def add_node(self, node: Node):
        self._nodes.append(node)
    
    def add_edge(self, src, dest) -> None:
        return
        