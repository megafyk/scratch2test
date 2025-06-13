class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # prefix sum + sliding window + bitmask
        # time O(n), space O(1)
        n = len(s)
        res = -sys.maxsize

        def get_status(a, b):
            return ((a & 1) << 1) | (b & 1)

        lst = "01234"
        for a in lst:
            for b in lst:
                if a == b:
                    continue

                cnt_a, cnt_b = 0, 0  # prefix sum freq at j in [i..j]
                cnt_prev_a, cnt_prev_b = 0, 0  # prefix sum freq and i in [i..j]
                min_diff = [sys.maxsize] * 4
                l = -1
                for r in range(n):
                    cnt_a += 1 if s[r] == a else 0
                    cnt_b += 1 if s[r] == b else 0

                    while (
                        r - l >= k and (cnt_b - cnt_prev_b) >= 2
                    ):  # implicit b is even
                        left_status = get_status(cnt_prev_a, cnt_prev_b)
                        min_diff[left_status] = min(
                            min_diff[left_status], cnt_prev_a - cnt_prev_b
                        )
                        l += 1
                        cnt_prev_a += 1 if s[l] == a else 0
                        cnt_prev_b += 1 if s[l] == b else 0

                    right_status = get_status(cnt_a, cnt_b)
                    req_left_status = right_status ^ 2
                    if min_diff[req_left_status] != sys.maxsize:
                        # Calculate the difference: (cnt_a-cnt_b) - min(prev_a-prev_b).
                        res = max(res, cnt_a - cnt_b - min_diff[req_left_status])

        return res
