class NumArray:

    def __init__(self, nums: List[int]):
        # calculate prefix sum
        # complexity: time O(n), mem O(n)
        self.p = [0]
        n = len(nums)
        for i in range(1, n+1):
            self.p.append(self.p[i-1] + nums[i-1])

    def sumRange(self, left: int, right: int) -> int:
        # complexity O(1)
        return self.p[right+1] - self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)