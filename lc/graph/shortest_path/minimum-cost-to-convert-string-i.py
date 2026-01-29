class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:    
        # djikstra
        # n = len(source)
        # e = len(changed)
        # time O(n + 26*eloge), space O(e)
        adj = defaultdict(list)
        for i in range(len(original)):
            pos_s = ord(original[i]) - ord('a')
            pos_t = ord(changed[i]) - ord('a')
            adj[pos_s].append((pos_t, cost[i]))
        
        inf = sys.maxsize
        def min_cost(c_pos):
            dist = [inf] * 26

            dist[c_pos] = 0
            pq = [(0, c_pos)]
            while pq:
                w, u = heappop(pq)
                for v,wv in adj[u]:
                    nw_w = w + wv
                    if nw_w < dist[v]:
                        dist[v] = nw_w
                        heappush(pq, (nw_w, v))
            return dist

        min_cost_map = defaultdict(int)
        for i in range(26):
            min_cost_map[i] = min_cost(i)

        cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            pos1 = ord(source[i]) - ord('a')
            pos2 = ord(target[i]) - ord('a')
            
            if min_cost_map[pos1][pos2] == inf:
                return -1

            cost += min_cost_map[pos1][pos2]
        return cost
class Solution1:
    def ch2int(self, c):
        return ord(c) - ord("a")

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # dp floyd warshall
        # complexity: time O(n), mem O(1)
        inf = float("inf")
        dp = [[inf] * 26 for _ in range(26)]
        for i in range(len(original)):
            u = self.ch2int(original[i])
            v = self.ch2int(changed[i])
            dp[u][v] = min(dp[u][v], cost[i])

        for i in range(len(original)):
            j = self.ch2int(original[i])
            dp[j][j] = 0

        for i in range(len(source)):
            j = self.ch2int(source[i])
            dp[j][j] = 0

        ans = 0

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        ans = 0
        for i in range(len(source)):
            tmp = dp[self.ch2int(source[i])][self.ch2int(target[i])]
            if tmp == inf:
                return -1
            ans += tmp
        return ans
