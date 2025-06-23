class Solution:
    def pushDominoes(self, d: str) -> str:
        # two pointers
        # time O(N), space O(1)
        i = 0
        res = []
        N = len(d)
        for j in range(N):
            if d[j] == 'R':
                if d[i] == '.' or d[i] == 'L':
                    res += d[i:j]
                else:
                    res += ['R'] * (j-i)
                i = j
            elif d[j] == 'L':
                if d[i] == 'R':
                    tmp = (j-i)
                    if tmp % 2 == 0:
                        res += ['R'] * (tmp//2) + ['.'] + ['L'] * (tmp//2)
                    else: 
                        res += ['R'] * (tmp//2 + 1) + ['L'] * (tmp//2 + 1)
                else:
                    res += ['L'] * (j-i+1)
                i = j+1

        if i < N: 
            if d[i] == 'L' or d[i] == '.':
                res += d[i:]
            else:
                res += ['R'] * (N-i)

        return ''.join(res)