class Solution:
    # def partition(self, nums, low, high):
    #     i = low
    #     pivot_idx = random.randint(low, high)
    #     pivot = nums[pivot_idx]
    #     nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

    #     for j in range(low, high):
    #         if nums[j] <= pivot:
    #             nums[i],nums[j] = nums[j],nums[i]
    #             i+=1
    #     nums[i], nums[high] = nums[high], nums[i]
    #     return i

    # def quicksort(self, nums, low, high):
    #     if low >= high:
    #         return

    #     pivot_idx = self.partition(nums, low, high)

    #     self.quicksort(nums, low, pivot_idx-1)
    #     self.quicksort(nums, pivot_idx+1, high)

    # def sortArray(self, nums: List[int]) -> List[int]:
    #     self.quicksort(nums, 0, len(nums)-1)
    #     return nums

    def mergesort(self, nums):
        # complexity: time O(nlogn), mem O(n)
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])

        ans = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        ans.extend(left[i:])
        ans.extend(right[j:])
        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
