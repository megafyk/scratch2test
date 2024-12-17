class Solution:
    def repeatLimitedString(self, s: str, repeat: int) -> str:
        # max heap + counting
        # time O(nlogn), space O(n)
        res = [""]
        cnt = Counter(s)
        pq = []
        for k,v in cnt.items():
            heappush(pq, (-ord(k), k, v))
        while pq:
            od,k,v = heappop(pq)
            if k != res[-1]:
                res += [k] * min(v, repeat)
                v -= min(v, repeat)
                if v > 0:
                    heappush(pq, (od, k, v))
            else:
                if pq:
                    od2,k2,v2 = heappop(pq)
                    res += k2
                    v2-=1
                    if v2 > 0:
                        heappush(pq, (od2,k2,v2))
                    heappush(pq, (od,k,v))
        return ''.join(res)
