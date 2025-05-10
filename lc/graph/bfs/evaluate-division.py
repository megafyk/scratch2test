from collections import deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # build graph
        graph = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            if a not in graph:
                graph[a] = []
            graph[a].append((b, values[i]))
            if b not in graph:
                graph[b] = []
            graph[b].append((a, 1/values[i]))

        res = []

        for c,d in queries:
            if c not in graph:
                res.append(-1)
                continue
            if c == d:
                res.append(1)
                continue
                
            q = deque([(c, 1)])
            visited = set()
            ans_for_query = -1
            while q:
                u,weight_u = q.popleft()
                visited.add(u)
                for v, weight_v in graph[u]:
                    if v in visited:
                        continue
                    weight_v *= weight_u
                    if v == d:
                        ans_for_query = weight_v
                        break
                    q.append((v, weight_v))
                    
            
            res.append(ans_for_query)

        return res

