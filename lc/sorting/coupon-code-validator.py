class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        # sorting
        # time O(nlogn), space O(n)
        res = []

        def valid_c(c):
            return (
                c == "_"
                or 97 <= ord(c) <= 122
                or 65 <= ord(c) <= 90
                or 48 <= ord(c) <= 57
            )

        bizz_map = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        def valid(idx):
            return code[idx] and isActive[idx] and (businessLine[idx] in bizz_map)

        for idx, co in enumerate(code):
            if not valid(idx):
                continue
            check = True
            for c in co:
                if not valid_c(c):
                    check = False
                    break
            if check:
                res.append((bizz_map[businessLine[idx]], co))

        res.sort(key=lambda x: (x[0], x[1]))
        return [A[1] for A in res]