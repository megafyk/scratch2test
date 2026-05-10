class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        # math seive
        # time O(nlogn + n*sqrt(nums[i])), space O(n)
        n = len(nums)
        s = SortedSet()

        mx = -1
        replace = defaultdict(int)
        for num in nums:
            if num == 1:
                return n
            s.add(num)
            mx = max(mx, num)
            replace[num] = num

        for num in s:
            mx_mul = mx // num
            if mx_mul <= 0:
                break

            for mul in range(1, mx_mul + 1):
                t = mul * num
                if t in s:
                    replace[t] = min(replace[t], num)

        total = 0
        for num in nums:
            total += replace[num]
        return total
