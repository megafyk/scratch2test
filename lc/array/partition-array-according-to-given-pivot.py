class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # array
        # time O(N), space O(N)
        smaller = []
        equal = []
        bigger = []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                bigger.append(num)
            else:
                equal.append(num)
        return smaller + equal + bigger


class Solution1:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        i = 0
        cnt_pivot = 0
        for x in nums:
            if x < pivot:
                res[i] = x
                i += 1
            elif x == pivot:
                cnt_pivot += 1

        for _ in range(cnt_pivot):
            res[i] = pivot
            i += 1

        for x in nums:
            if x > pivot:
                res[i] = x
                i += 1

        return res
