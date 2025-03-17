class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # bitwise
        # space O(N), space O(1)
        check = 0
        for num in nums:
            check ^= (1 << num)
        return check == 0

    # def divideArray(self, nums: List[int]) -> bool:
    #     # array + hashtable
    #     # time O(N), space O(N)
    #     check = defaultdict(int)
    #     for num in nums:
    #         if num in check:
    #             check.pop(num)
    #         else:
    #             check[num] = 1
    #     return len(check) == 0
