class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        arr = [(positions[i], healths[i], directions[i]) for i in range(n)]
        arr.sort()
        st = []

        for i in range(n):
            pos, hea, di = arr[i]
            append = True
            while st and st[-1][-1] == "R" and di == "L":
                p, h, d = st.pop()
                if h == hea:
                    append = False
                    break
                elif h > hea:
                    pos = p
                    hea = h - 1
                    di = d
                    break
                else:
                    hea -= 1
            if append:
                st.append((pos, hea, di))

        h_map = defaultdict(int)
        for p, h, _ in st:
            h_map[p] = h
        res = []
        for p in positions:
            if h_map[p] > 0:
                res.append(h_map[p])
        return res
