class Solution:
    def minimumCost(self, c1: int, c2: int, c3: int, n1: int, n2: int) -> int:
        min_cost = min(c1 + c2, c3) * min(n1, n2)
        if n1 > n2:
            min_cost += min(c1, c3) * (n1 - n2)
        else:
            min_cost += min(c2, c3) * (n2 - n1)
        return min_cost
            
class Solution1:
    def minimumCost(self, c1: int, c2: int, c3: int, n1: int, n2: int) -> int:
        x = c1 + c2 - c3
        y = n1 * c1 + n2 * c2
        if x <= 0: 
            return y
        else:
            l,r = 0, min(n1, n2)
            while l < r:
                mid = l + (r - l + 1) // 2
                if mid * x <= y:
                    l = mid
                else:
                    r = mid - 1
            return min(y - l * x, c3 * max(n1, n2))
            