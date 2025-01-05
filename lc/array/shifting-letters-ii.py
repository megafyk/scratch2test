class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # prefix sum accumulate shifts
        # time O(m), space O(n)
        n = len(s)
        prefix = [0] * (n+1)
        encode = [(ord(s[i]) - ord('a')) for i in range(n)]

        # apply shift to all s[i]
        for s,e,di in shifts:
            prefix[e+1] += 1 if di == 1 else -1
            prefix[s] += -1 if di == 1 else 1

        prefix_idx = n
        diff = prefix[prefix_idx]
        for i in range(n-1, -1, -1):
            encode[i] += diff
            prefix_idx -= 1
            diff += prefix[prefix_idx]
        # decode
        decode = [chr(((c + 26) % 26) + ord('a')) for c in encode]
        return ''.join(decode)
