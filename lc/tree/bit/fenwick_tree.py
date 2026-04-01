class FenwickTree:
    """Binary Indexed Tree (Fenwick Tree) for prefix sum queries and point updates.

    Supports O(log n) point updates and O(log n) prefix sum queries.
    Accepts 0-based indices externally; converts to 1-based internally.

    Attributes:
        n: Number of elements.
        bit: Internal 1-based array storing partial sums.
    """

    def __init__(self, n):
        """Initialize a Fenwick tree of size n with all zeros.

        Args:
            n: Number of elements in the array.
        """
        self.n = n
        self.bit = [0] * (n + 1)
    
    def get_sum(self, p):
        """Return the prefix sum from index 0 to p (inclusive).

        Args:
            p: 0-based index (inclusive upper bound).

        Returns:
            Sum of elements in arr[0..p].
        """
        idx = p + 1
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= (idx & (-idx))
        return ans
    
    def update(self, p, v):
        """Add v to the element at index p.

        Args:
            p: 0-based index of the element to update.
            v: Value to add (use new - old to set a specific value).
        """
        idx = p + 1
        while idx <= self.n:
            self.bit[idx] += v
            idx += (idx & (-idx))

def main():
    arr = [8,4,1,24,6,9,10] 
    tree = FenwickTree(len(arr))
    for i, num in enumerate(arr):
        tree.update(i, num)
    print(tree.get_sum(6))
    print(tree.get_sum(2))
    tree.update(2, 3-arr[2])
    print(tree.get_sum(2))

if __name__ == "__main__":
    main()
        