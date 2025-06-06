class Solution:
    def robotWithString(self, s: str) -> str:
        # greedy + stack + freq
        # time O(n), space O(n)
        freq = Counter(s)
        min_ch = "a"
        t = []
        res = []
        for c in s:
            freq[c] -= 1
            t.append(c)
            while min_ch != "z" and freq[min_ch] == 0:
                min_ch = chr(ord(min_ch) + 1)

            while t and t[-1] <= min_ch:
                res.append(t.pop())

        return "".join(res)
