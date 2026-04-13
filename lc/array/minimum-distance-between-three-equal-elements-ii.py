class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # time O(n) space O(n)
        eq_idx = defaultdict(list)
        res = inf
        for idx, num in enumerate(nums):
            eq_idx[num].append(idx)
            if len(eq_idx[num]) >= 3:
                #dist = abs(eq_idx[num][-1] - eq_idx[num][-2]) + abs(eq_idx[num][-2] - eq_idx[num][-3]) + abs(eq_idx[num][-3] - eq_idx[num][-1])
                dist = 2 * (eq_idx[num][-1] - eq_idx[num][-3])
                res = min(res, dist)
        return res if res != inf else -1
        
class Solution1:
    def minimumDistance(self, nums: List[int]) -> int:
        # sorting
        # time O(nlogn) space O(n)
        n = len(nums)
        if n < 3: return -1
        arr = sorted([(nums[i], i) for i in range(n)])
        res = sys.maxsize
        for k in range(2, n):
            if arr[k][0] == arr[k-1][0] == arr[k-2][0]:
                res = min(res, abs(arr[k][1] - arr[k-1][1]) + abs(arr[k-1][1] - arr[k-2][1]) + abs(arr[k-2][1] - arr[k][1]))
        return res if res != sys.maxsize else -1
        