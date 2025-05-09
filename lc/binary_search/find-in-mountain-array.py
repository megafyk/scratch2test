# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, m: 'MountainArray') -> int:
        # binary search
        # time O(logN), space O(1)
        
        # find cut point
        l,r = 1, m.length() - 2
        
        while l <= r:
            mid = l + (r-l) // 2

            l_val = m.get(mid-1)
            r_val = m.get(mid+1)
            mid_val = m.get(mid)

            if l_val < mid_val > r_val:
                cut = mid
                break
            elif l_val < mid_val < r_val:
                l = mid + 1
            else:
                r = mid - 1
                
        # left search
        l,r = 0, cut
        while l<=r:
            mid = l + (r-l) // 2
            if m.get(mid) == target:
                return mid
            elif m.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1

        # right search
        l,r = cut, m.length() - 1
        while l <= r:
            mid = l + (r-l) // 2
            if m.get(mid) == target:
                return mid
            elif m.get(mid) > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1