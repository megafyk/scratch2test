from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minimum = threshold * k
        ans = 0
        left = 0
        right = k - 1

        curr_sum = sum(arr[left:right + 1])

        while right < len(arr):
            if curr_sum >= minimum:
                ans += 1

            curr_sum -= arr[left]

            left += 1
            right += 1

            if right < len(arr):
                curr_sum += arr[right]

        return ans


s = Solution()
print(s.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
