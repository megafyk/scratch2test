class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # matrix + bfs
        # time O((m+n)*(m+n)!), space O((m+n)*(m+n)!)
        adj = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]

        b = ""
        for i in range(2):
            for j in range(3):
                b += str(board[i][j])

        q = deque([(b.index("0"), 0, b)])
        visit = set([b])
        while q:
            idx,d,state = q.popleft()

            if state == "123450":
                return d

            b_arr = list(state)

            for u in adj[idx]:
                b_arr[idx], b_arr[u] =  b_arr[u], b_arr[idx]
                new_b = ''.join(b_arr)
                if new_b not in visit:
                    q.append((u, d+1, new_b))
                    visit.add(new_b)
                b_arr[idx], b_arr[u] =  b_arr[u], b_arr[idx]

        return -1
