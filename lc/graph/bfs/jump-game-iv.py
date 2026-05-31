class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        pos = defaultdict(list)
        for i, num in enumerate(arr):
            pos[num].append(i)

        q = deque([(0, 0)])
        visit = set()
        while q:
            u, step = q.popleft()
            if u == n - 1:
                return step
            if u > 0 and (u - 1) not in visit:
                q.append((u - 1, step + 1))
                visit.add(u - 1)
            if u < n - 1 and (u + 1) not in visit:
                q.append((u + 1, step + 1))
                visit.add(u + 1)
            for v in pos[arr[u]]:
                if v not in visit:
                    q.append((v, step + 1))
                    visit.add(v)
            pos[arr[u]] = []
        return -1
