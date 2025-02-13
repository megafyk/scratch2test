import bisect

class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        # hashtable + sorted set
        # time O(nlogn), space O(n)
        def sum_digits(num):
            total = 0
            for d in str(num):
                total += int(d)
            return total

        hm = defaultdict(list)
        for num in nums:
            sum_digit = sum_digits(num)
            if sum_digit in hm:
                bisect.insort(hm[sum_digit], num)
            else:
                hm[sum_digit].append(num)

        res = -1
        for lst in hm.values():
            if len(lst) >= 2:
                res = max(res, lst[-1] + lst[-2])
        return res