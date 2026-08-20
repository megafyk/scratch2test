class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        mx_group = n * 2
        row_reserved_pos = defaultdict(list)
        for r, seat in reservedSeats:
            row_reserved_pos[r].append(seat)
        g1 = {2,3,4,5}
        g2 = {4,5,6,7}
        g3 = {6,7,8,9}
        for arr in row_reserved_pos.values():
            gg1 = gg2 = gg3 = True
            for p in arr:
                if p in g1: gg1 = False
                if p in g2: gg2 = False
                if p in g3: gg3 = False

            sub = 2
            if gg1 and gg3:
                sub = 0
            elif gg1 or gg2 or gg3:
                sub = 1
            mx_group -= sub


        return mx_group
