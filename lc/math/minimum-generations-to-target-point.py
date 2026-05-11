class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        # brute force
        # time = 7!*7!*7!, space = 7!
        n = len(points)
        if n == 1:
            if points[0] == target:
                return 0
            return -1
        k = 0
        s = set()
        for x, y, z in points:
            s.add((x, y, z))
        target = (target[0], target[1], target[2])
        if target in s:
            return 0
        k = 1
        while True:
            s_tmp = set()
            for x1, y1, z1 in s:
                for x2, y2, z2 in s:
                    if (x1, y1, z1) != (x2, y2, z2):
                        x = (x1 + x2) // 2
                        y = (y1 + y2) // 2
                        z = (z1 + z2) // 2
                        if (x, y, z) == target:
                            return k
                        if (x, y, z) not in s:
                            s_tmp.add((x, y, z))
            if len(s_tmp) == 0:  # no gain new node
                return -1
            else:
                s.update(s_tmp)
            k += 1
