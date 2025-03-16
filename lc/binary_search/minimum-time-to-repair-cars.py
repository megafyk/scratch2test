class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # binary search
        # time O(rlogn), space O(1)
        left, right = 1, max(ranks)* cars * cars

        def can_fix(time):
            cnt = 0
            for r in ranks:
                cnt += int((time // r) ** 0.5)
            return cnt >= cars

        while left < right:
            mid = left + (right - left) // 2
            if can_fix(mid):
                right = mid
            else:
                left = mid + 1
        return left