import sys


class SegmentTree:
    """A segment tree supporting range minimum queries and point updates.

    Uses 1-based indexing internally with a flat array of size 4*N.
    Each node stores the minimum value of its corresponding range.

    Attributes:
        arr: The original input array.
        st: The internal segment tree array.
    """

    def __init__(self, arr):
        """Initialize the segment tree with the given array.

        Args:
            arr: List of comparable elements to build the tree from.
        """
        self.arr = arr
        N = len(arr)
        self.st = [0] * 4 * N

    def build(self, id, l, r):
        """Recursively build the segment tree.

        Args:
            id: Current node index in the tree (1-based).
            l: Left boundary of the current segment.
            r: Right boundary of the current segment.
        """
        if l == r:  # leaf
            self.st[id] = self.arr[l]
            return
        mid = l + (r - l) // 2
        self.build(2 * id, l, mid)
        self.build(2 * id + 1, mid + 1, r)
        self.st[id] = min(self.st[2 * id], self.st[2 * id + 1])

    def update(self, id, l, r, i, val):
        """Update the value at index i to val.

        Args:
            id: Current node index in the tree (1-based).
            l: Left boundary of the current segment.
            r: Right boundary of the current segment.
            i: Index in the original array to update.
            val: New value to set at index i.
        """
        if i < l or i > r:
            return
        if l == r == i:
            self.st[id] = val
            self.arr[i] = val  # sync with original
            return
        mid = l + (r - l) // 2
        self.update(2 * id, l, mid, i, val)
        self.update(2 * id + 1, mid + 1, r, i, val)
        self.st[id] = min(self.st[2 * id], self.st[2 * id + 1])

    def get(self, id, l, r, u, v):
        """Query the minimum value in the range [u, v].

        Args:
            id: Current node index in the tree (1-based).
            l: Left boundary of the current segment.
            r: Right boundary of the current segment.
            u: Left boundary of the query range (inclusive).
            v: Right boundary of the query range (inclusive).

        Returns:
            The minimum value in arr[u..v].
        """
        if l > v or r < u:
            return sys.maxsize
        if u <= l <= r <= v:
            return self.st[id]
        mid = l + (r - l) // 2
        f1 = self.get(2 * id, l, mid, u, v)
        f2 = self.get(2 * id + 1, mid + 1, r, u, v)
        return min(f1, f2)


def main():
    arr = [9, 2, 6, 3, 1, 5, 7]
    tree = SegmentTree(arr)
    l, r = 0, len(arr) - 1
    tree.build(1, l, r)
    print(tree.get(1, l, r, 2, 6))
    tree.update(1, l, r, 4, 8)
    print(tree.get(1, l, r, 2, 6))


if __name__ == "__main__":
    main()
