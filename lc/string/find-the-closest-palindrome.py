class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # tricky problems
        # complexity: O(1), mem O(1)
        m = len(n)
        candidates = []

        left = n[: m // 2]
        if m % 2 == 0:
            for delta in [-1, 0, 1]:
                new_left = str(int(left) + delta)
                candidates.append(new_left + new_left[::-1])

        else:
            mid = n[m // 2]
            for delta in [-1, 0, 1]:
                new_mid = int(mid) + delta
                if 0 <= new_mid <= 9:
                    candidates.append(left + str(new_mid) + left[::-1])

        if m > 1:
            candidates.append("9" * (m - 1))
        candidates.append("1" + "0" * (m - 1) + "1")

        min_abs = sys.maxsize
        num = int(n)
        ans = ""

        for can in candidates:
            temp = abs(num - int(can))
            if (temp < min_abs and temp > 0) or (
                temp == min_abs and temp > 0 and int(can) < int(ans)
            ):
                ans = can
                min_abs = temp
        return ans
