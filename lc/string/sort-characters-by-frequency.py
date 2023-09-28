class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}
        for l in s:
            if l in freq:
                freq[l] += 1
            else:
                freq[l] = 1

        # freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        bucket = [[] for _ in range(len(s) + 1)]

        for k, v in freq.items():
            bucket[v].append(k)

        res = ''
        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                res += bucket[i][j] * i
        return res


s = Solution()
print(s.frequencySort("tree"))
