class Solution:

    def is_prime(self, num):
        if num <= 1: return False
        if num == 2: return True
        if num % 2 == 0: return False
        for i in range(3, int(math.sqrt(num)) + 1):
            if num % i == 0: return False
        return True

    def prime(self):
        p_nums = [2]
        for i in range(3, 1111, 2):
            if self.is_prime(i):
                p_nums.append(i)
        return p_nums

    def primeSubOperation(self, nums: List[int]) -> bool:
        # prime + binary search
        # time O(n*sqrt(n) + nlogn), space O(n)
        p_nums = self.prime()
        nums = [0] + nums
        for i in range(1, len(nums)):
            l, r = 0, len(p_nums)
            while l < r:
                mid = l + (r-l) // 2
                if nums[i] - p_nums[mid] <= nums[i-1]:
                    r = mid
                else:
                    l = mid + 1
            if l == 0:
                if nums[i] <= nums[i-1] and i < len(nums):
                    return False
            if l != 0:
                nums[i] -= p_nums[l-1]
        return True
