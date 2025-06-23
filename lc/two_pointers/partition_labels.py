class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pointers
        # time O(N), space O(1)

        res = []
        last = defaultdict(int)
        for i,c in enumerate(s):
            last[c] = i
        size,end = 0,0
        for i,c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                res.append(size)
                size = 0
        
        return res