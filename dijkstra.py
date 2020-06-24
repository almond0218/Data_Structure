from __future__ import annotations

from heapq import heapify
from heapq import heappop
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union


class Node:
    """다익스트라 알고리즘에 사용되는 클래스다."""

    def __init__(self, key: int):
        self.key = key
        self.edges = {}

    def __lt__(self, other: Node):
        return self.key < other.key

    def add_edge(self, target: int, cost: int):
        """

        Args:
            target: 목표 노드의 키값
            cost: 엣지의 비용
        """
        self.edges[target] = cost


# noinspection PyTypeChecker
class Dijkstra:
    def __init__(self, nodes: List[Node], source: int = 0):
        self.source = source
        self.distances = [0 if i == source else float("inf") for i in range(len(nodes))]
        self.parents = [None for _ in range(len(nodes))]
        self.queue = [(self.distances[node.key], node) for node in nodes]
        heapify(self.queue)

    def process(self) -> Tuple[List[Union[int, float]], List[Optional[int]]]:
        """다익스트라 알고리즘을 실행하는 메서드
        큐에서 거리가 가장 짧은 노드부터 순차적으로 꺼내서 각 엣지를 릴렉스 한다.

        Returns:
            (tuple(list, list)): 각 노드들의 거리와 각 노드들의 부모를 가지고 있는 튜플
        """
        while self.queue:
            _, current_node = heappop(self.queue)
            for target_node_key, edge_cost in current_node.edges.items():
                current_node_distance = self._get_distance_from_key(current_node.key)
                self._relax(
                    current_node.key, current_node_distance, target_node_key, edge_cost
                )
        return self.distances, self.parents

    def _relax(
        self,
        current_node_key: int,
        current_node_distance: Union[int, float],
        target_node_key: int,
        edge_cost: int,
    ):
        """목표 노드의 거리와 엣지의 비용을 비교해서 엣지의 비용이 더 작을 경우 목표 노드의 거리를 현재 엣지의 비용으로 변경한다.

        Args:
            current_node_key: 현재 노드의 키값
            current_node_distance: 소스부터 현재 노드까지의 거리
            target_node_key: 목표 노드의 키값
            edge_cost: 엣지의 비용
        """
        target_node_distance = self._get_distance_from_key(target_node_key)
        cost = current_node_distance + edge_cost
        if target_node_distance > cost:
            self._set_distance(target_node_key, cost)
            self._set_parent(target_node_key, current_node_key)
            self._reset_queue()

    def _get_distance_from_key(self, key: int) -> Union[int, float]:
        """노드의 키값으로부터 거리를 가져온다.

        Args:
            key: 거리를 가져오고 싶은 노드의 키값

        Returns:
            (int or float): 노드의 거리
        """
        return self.distances[key]

    def _set_distance(self, key: int, distance: int):
        """노드의 거리를 변경한다.

        Args:
            key: 변경할 노드의 키값
            distance: 변경할 거리
        """
        self.distances[key] = distance

    def _set_parent(self, key: int, parent_key: int):
        """노드의 부모를 변경한다.

        Args:
            key: 변경할 노드의 키값
            parent_key: 노드에 저장할 부모 노드의 키
        """
        self.parents[key] = parent_key

    def _reset_queue(self):
        """큐를 재설정한다.
        큐를 재설정 하는 이유는 각 노드들의 거리가 변경될 때마다 반영하기 위함이다.
        """
        self.queue = [(self.distances[node.key], node) for _, node in self.queue]
        heapify(self.queue)


class App:
    def __init__(self):
        num_nodes = int(input())
        nodes = [Node(i) for i in range(num_nodes)]

        num_edges = int(input())
        for _ in range(num_edges):
            key, target, cost = map(int, input().split())
            nodes[key].add_edge(target, cost)

        d = Dijkstra(nodes)
        distances, parents = d.process()
        print("distances: {}".format(distances))
        print("parents: {}".format(parents))


App()
