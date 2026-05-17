class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs
        # time O(n), space O(n)
        visit = set()
        q = deque()
        q.append(start)
        n = len(arr)
        visit.add(start)
        while q:
            u = q.popleft()

            if arr[u] == 0:
                return True

            for v in [u-arr[u], u+arr[u]]:
                if 0 <= v < n and v not in visit:
                    q.append(v)
                    visit.add(v)
        return False
