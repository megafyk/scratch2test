from collections import defaultdict
from typing import List


class Solution:
    def countSequences(self, nums: List[int], K: int) -> int:
        n = len(nums)

        x = defaultdict(int)
        y = defaultdict(int)

        def dfs(i):
            if i == n:
                xx = 1
                for k, v in x.items():
                    if k in y:
                        v -= min(v, y[k])
                    xx *= k**v

                yy = 1
                for k, v in y.items():
                    if k in x:
                        v -= min(v, x[k])
                    yy *= k**v

                if xx / yy == K:
                    return 1
                return 0

            cnt = 0
            x[nums[i]] += 1
            cnt += dfs(i + 1)
            x[nums[i]] -= 1

            y[nums[i]] += 1
            cnt += dfs(i + 1)
            y[nums[i]] -= 1

            cnt += dfs(i + 1)
            return cnt

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    nums = [5, 3, 3, 5, 4, 1, 2, 6, 6, 6, 6]
    k = 2
    import time
    start_time = time.perf_counter()
    res = s.countSequences(nums, k)
    end_time = time.perf_counter()
    print(res, end_time - start_time)
