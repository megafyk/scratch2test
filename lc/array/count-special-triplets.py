class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = Counter()
        right = Counter(nums)
        res = 0
        mod = 10 ** 9 + 7
        for num in nums:
            right[num] -= 1
            t = num * 2
            res = (res + (left[t] * right[t]) % mod) % mod
            left[num] += 1
        return res
    
class Solution1:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        num_idx = defaultdict(list)
        for idx, num in enumerate(nums):
            num_idx[num].append(idx)
        
        res = 0
        if 0 in num_idx:
            l = len(num_idx[0])
            res = (((l-2)*(l-1)*l) // 6) % mod

        n = len(nums)
        
        for j in range(n):
            if nums[j] != 0:
                t = nums[j] * 2
                if t in num_idx:
                    arr = num_idx[t]
                    if arr[0] < j < arr[-1]:
                        idx = bisect.bisect_left(arr, j)
                        res = (res + (idx * (len(arr) - idx)) % mod) % mod
        
        return res % mod
