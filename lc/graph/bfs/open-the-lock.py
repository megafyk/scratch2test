class Solution:
    def open_lock(self, deadends: List[str], target: str) -> int:
        # graph bfs
        # time O(n), space O(n)
        dead = set(deadends)
        if "0000" in dead: return -1
        dead.add("0000")
        q = deque([("0000", 0)])

        while q:
            cur, turn = q.popleft()
            if cur == target:
                return turn

            for i in range(4):
                d = int(cur[i])
                
                d_up = (d+1) % 10
                nw_up = cur[:i] + str(d_up) + cur[i+1:]
                if nw_up not in dead:
                    q.append((nw_up, turn+1))
                    dead.add(nw_up)

                d_down = (d-1) % 10
                nw_down = cur[:i] + str(d_down) + cur[i+1:]
                if nw_down not in dead:
                    q.append((nw_down, turn+1))
                    dead.add(nw_down)

        return -1