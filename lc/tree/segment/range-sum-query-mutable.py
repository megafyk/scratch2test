class NumArray:
    def construct(self, nums, st, pos, l, r):
        if l == r:
            st[pos] = nums[l]
            return nums[l]

        mid = l + (r - l) // 2
        st[pos] = self.construct(nums, st, 2 * pos + 1, l, mid) + self.construct(nums, st, 2 * pos + 2, mid + 1, r)
        return st[pos]

    def updateTree(self, st, pos, l, r, index, diff):
        if index < l or index > r:  # Skip if out of range
            return
        st[pos] += diff
        if l != r:  # If not a leaf node
            mid = l + (r - l) // 2
            self.updateTree(st, 2 * pos + 1, l, mid, index, diff)
            self.updateTree(st, 2 * pos + 2, mid + 1, r, index, diff)

    def query(self, st, pos, l, r, ql, qr):
        if l >= ql and r <= qr:  # Full overlap
            return st[pos]
        if l > qr or r < ql:  # No overlap
            return 0
        # Partial overlap
        mid = l + (r - l) // 2
        return self.query(st, 2 * pos + 1, l, mid, ql, qr) + self.query(st, 2 * pos + 2, mid + 1, r, ql, qr)

    def __init__(self, nums: List[int]):
        # Construct segment tree
        self.nums = nums
        n = len(self.nums)
        self.st = [0] * (4 * n)  # Allocate sufficient space
        self.construct(self.nums, self.st, 0, 0, n - 1)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateTree(self.st, 0, 0, len(self.nums) - 1, index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(self.st, 0, 0, len(self.nums) - 1, left, right)
