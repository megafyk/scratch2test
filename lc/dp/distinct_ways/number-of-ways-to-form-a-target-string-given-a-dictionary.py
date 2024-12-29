class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # dp top down distinct ways
        # time O(n*k), space O(n*k)
        mod = 10 ** 9 + 7
        m = len(words)
        n = len(words[0])
        k = len(target)
        freq = []

        for i in range(n):
            freq_col = defaultdict(int)
            for j in range(m):
                freq_col[words[j][i]] += 1
            freq.append(freq_col)

        @cache
        def count(idx, t_pos):
            if t_pos == k:
                return 1
            if t_pos < k and idx >= n:
                return 0

            ch = target[t_pos]
            include = skip = 0
            if ch not in freq[idx]:
                skip += count(idx+1, t_pos)
            else:
                include += count(idx+1,t_pos+1) * freq[idx][ch] # optimize by not recalculate ch
                skip += count(idx+1,t_pos)

            return include + skip

        return count(0, 0) % mod
