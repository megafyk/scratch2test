class Solution:
    def pos(self, c):
        return ord(c) - ord('a')

    def partitionLabels(self, s: str) -> List[int]:
        # complexity: time O(n), mem O(1)
        n = len(s)
        res = []

        last = {}
        for i in range(n):
            last[s[i]] = i
        
        i,j = 0,0
        res = []
        for i in range(n):
            target = s[i]
            while j < n:
                if last[target] < last[s[j]]:
                    target = s[j]

                if s[j] == target and j == last[target]:
                    res.append(j-i+1)
                    i,j = j+1, j+1
                else:
                    j+=1

        return res

