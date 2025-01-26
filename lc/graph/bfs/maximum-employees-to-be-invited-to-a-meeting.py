class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        longest_cycle = 0
        visit = [False] * N
        length_2_cycles = []
        # find longest cycle
        for i in range(N):
            if visit[i]:
                continue
            start, cur = i,i
            cur_set = set()
            while not visit[cur]:
                visit[cur] = True
                cur_set.add(cur)
                cur = favorite[cur]

            if cur in cur_set:
                length = len(cur_set)
                while start != cur:
                    length -= 1
                    start = favorite[start]
                longest_cycle = max(longest_cycle, length)
                if length == 2:
                    length_2_cycles.append([cur, favorite[cur]])

        # find sum of longest non closed cycle
        inverted = defaultdict(list)
        for dst,src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src, par):
            q = deque([(src, 0)])
            max_length = 0
            while q:
                node, length = q.popleft()
                max_length = max(max_length, length)
                for nei in inverted[node]:
                    if nei != par:
                        q.append((nei, length + 1))
            return max_length


        chain_sum = 0
        for n1,n2 in length_2_cycles:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chain_sum, longest_cycle)
