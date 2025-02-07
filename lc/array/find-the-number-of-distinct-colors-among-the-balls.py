class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # array with hashmap
        # time O(N), space O(N)
        res = []
        ball_color = defaultdict(int)
        colors = defaultdict(int)
        for x,y in queries:
            if x in ball_color:
                prev = ball_color[x]
                colors[prev] -= 1
                if colors[prev] == 0:
                    colors.pop(prev)
            ball_color[x] = y
            colors[y] += 1
            res.append(len(colors))
        return res
                