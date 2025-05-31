class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # graph bfs
        # time O(n*n), space O(n*n)
        n = len(board)
        q = deque([1])

        step = 0
        visit = {1}
    
        def cord(val):
            x,y = divmod(val-1, n)
            if x % 2 == 0: return n-1-x,y
            return n-1-x,n-1-y

        while q:
            for _ in range(len(q)):
                label = q.popleft()
                x,y = cord(label)
                if board[x][y] != -1:
                   label = board[x][y]
                if label == n ** 2: return step
                for nxt in range(label + 1, min(label+6, n**2) + 1):
                    if nxt not in visit:
                        visit.add(nxt)
                        q.append(nxt)
            step += 1
        return -1