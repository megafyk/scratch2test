from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        visited = [float("inf")] * n
        visited[src] = 0

        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        queue = deque([(src, 0)])

        for _ in range(k + 1):
            size = len(queue)
            while size > 0:
                curr_node, curr_price = queue.popleft()
                for neighbor, price in adj[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[neighbor]:
                        visited[neighbor] = new_price
                        queue.append((neighbor, new_price))
                size -= 1

        return visited[dst] if visited[dst] != float("inf") else -1
