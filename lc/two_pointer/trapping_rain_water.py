from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        p_left = left = 0
        p_right = right = len(height) - 1
        ans = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] < height[p_left]:
                    ans += height[p_left] - height[left]
                else:
                    p_left = left
                left += 1
            else:
                if height[right] < height[p_right]:
                    ans += height[p_right] - height[right]
                else:
                    p_right = right
                right -= 1

        return ans


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
