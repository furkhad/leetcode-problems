import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph with both normal and reversed edges
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            # Normal traversal: u -> v with cost w
            graph[u].append((v, w))
            # Switch traversal: v -> u with cost 2 * w
            # (Reverses the incoming edge u->v to become v->u)
            graph[v].append((u, 2 * w))
            
        # Dijkstra's Algorithm initialization
        # Priority Queue stores tuples of (current_cost, current_node)
        pq = [(0, 0)]
        
        # Array to track minimum cost to reach each node
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        
        while pq:
            d, u = heapq.heappop(pq)
            
            # Optimization: If we found a shorter path to u previously, skip this one
            if d > min_cost[u]:
                continue
            
            # If we reached the target node, return the cost
            if u == n - 1:
                return d
            
            # Explore neighbors
            for v, weight in graph[u]:
                new_cost = d + weight
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
                    
        # If destination is unreachable
        return -1
