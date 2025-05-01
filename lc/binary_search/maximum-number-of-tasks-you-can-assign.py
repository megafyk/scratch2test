class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # binary search + monotonic queue
        
        tasks = sorted(tasks)
        workers = sorted(workers)

        def can_finish(task):
            p = 0 # count pills
            q = deque()
            j = len(workers) - 1
            for i in range(task-1, -1, -1):
                # match strongest task vs strongest worker
                while j >= len(workers) - task and (tasks[i] <= workers[j] or tasks[i] <= workers[j] + strength):
                    # decrease monotonic queue
                    q.appendleft(workers[j])
                    j -= 1
                if not q: return False
                if tasks[i] <= q[-1]:
                    q.pop()
                elif p < pills:
                    q.popleft()
                    p += 1
                else:
                    return False
            return True

        l, r = 0, min(len(tasks), len(workers))
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            if can_finish(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
