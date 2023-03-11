from typing import Optional, Dict, List


class GraphError(Exception):
    pass


class Graph:
    def __init__(
        self,
        adjacencies_list: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        self.adjacencies_list = adjacencies_list or {}

    def _print_graph(self):
        for vertex, neighbours in self.adjacencies_list.items():
            print(f"{vertex}: {neighbours}")

    def _are_neighbours(
        self,
        vertex: str,
        other_vertex: str,
    ) -> bool:
        if vertex not in self.adjacencies_list:
            raise GraphError(f"Vertex {vertex} does not exist")
        if other_vertex not in self.adjacencies_list:
            raise GraphError(f"Vertex {other_vertex} does not exist")
        return (
            other_vertex in self.adjacencies_list[vertex]
            and vertex in self.adjacencies_list[other_vertex]
        )

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adjacencies_list:
            self.adjacencies_list[vertex] = []
            return True
        return False

    def add_edge(
        self,
        vertex: str,
        other_vertex: str,
    ) -> bool:
        if (
            vertex in self.adjacencies_list
            and other_vertex in self.adjacencies_list
        ):
            if not self._are_neighbours(
                vertex=vertex,
                other_vertex=other_vertex,
            ):
                self.adjacencies_list[vertex].append(other_vertex)
                self.adjacencies_list[other_vertex].append(vertex)
                return True
        return False

    def remove_vertex_neighbour(
        self,
        vertex: str,
        neighbour: str,
    ) -> bool:
        if vertex not in self.adjacencies_list:
            return False

        if neighbour in self.adjacencies_list[vertex]:
            self.adjacencies_list[vertex].remove(neighbour)
            return True
        return False

    def remove_edge(
        self,
        vertex: str,
        other_vertex: str,
    ) -> bool:
        if (
            vertex in self.adjacencies_list
            and other_vertex in self.adjacencies_list
        ):
            self.remove_vertex_neighbour(
                vertex=vertex,
                neighbour=other_vertex,
            )
            self.remove_vertex_neighbour(
                vertex=other_vertex,
                neighbour=vertex,
            )
            return True
        return False

    def remove_vertex(self, vertex: str) -> bool:
        if vertex in self.adjacencies_list:
            vertex_neighbours = self.adjacencies_list[vertex].copy()
            for neighbour in vertex_neighbours:
                self.remove_edge(
                    vertex=vertex,
                    other_vertex=neighbour,
                )
            del self.adjacencies_list[vertex]
            return True
        return False

    def breath_first_search(self, vertex: str) -> List[str]:
        visited = set(vertex)
        queue = [vertex]
        while queue:
            current = queue.pop(0)
            for neighbour in self.adjacencies_list[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        return list(visited)

    def depth_first_search(self, vertex: str) -> List[str]:
        visited = set(vertex)
        stack = [vertex]
        while stack:
            current = stack.pop()
            for neighbour in self.adjacencies_list[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        return list(visited)
