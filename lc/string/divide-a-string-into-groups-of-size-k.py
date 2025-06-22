class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # string
        # time O(n), space O(1)
        res = []
        cur = ""
        for i in range(len(s)):
            cur += s[i]
            if len(cur) == k:
                res.append(cur)
                cur = ""

        if len(cur) > 0 and len(cur) < k:
            cur += fill * (k-len(cur))
            res.append(cur)
        return res