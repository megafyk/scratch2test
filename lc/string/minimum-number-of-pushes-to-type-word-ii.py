from collections import Counter
from heapq import *


class Solution:
    def minimumPushes(self, word: str) -> int:
        # pq
        # complexity: time O(n), mem O(1)
        cnt = Counter(word)
        ans = 0
        pq = []

        for ch, count in cnt.items():
            heappush(pq, (-count, ch))

        kb = [[] for _ in range(12)]
        i = 1
        while pq:
            if i > 8:
                i = 1
            count, ch = heappop(pq)
            kb[i].append((ch, -count))
            i += 1

        ans = 0
        for key in kb:
            for i in range(len(key)):
                ans += key[i][1] * (i + 1)
        return ans
