class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        # array
        # time O(n), space O(n)
        def count_change(arr, target):
            n = len(arr)
            change = 0
            for i in range(n - 1):
                if arr[i] != target:
                    arr[i + 1] *= -1
                    arr[i] *= -1
                    change += 1
            return (
                change if arr[-1] == target else sys.maxsize
            )  # all must num == target

        t1, t2 = count_change(list(nums), 1), count_change(nums, -1)
        return t1 <= k or t2 <= k
