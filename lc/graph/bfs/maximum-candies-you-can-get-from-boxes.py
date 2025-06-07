class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # graph bfs
        # time O(n), space O(n)
        n = len(status)
        cnt = 0
        q = deque()
        have = [False] * n
        box_locked = set()

        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                box_locked.add(box)
        
        while q:
            u = q.popleft()
            cnt += candies[u]
            
            for b in containedBoxes[u]:
                if not have[b]:
                    have[b] = True
                    if status[b] == 1:
                        q.append(b)
                    else:
                        box_locked.add(b)
                    
            for b in keys[u]:
                if status[b] == 0:
                    status[b] = 1
                    if b in box_locked:
                        q.append(b)

        return cnt
                
