from math import log2

class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        # time O(n), space O(n)
        m = int(log2(n)) + 1  # Maximum power of 2 needed
        self.dp = [[-1] * m for _ in range(n)]  # Binary lifting table

        # Initialize the direct parent
        for i in range(n):
            self.dp[i][0] = parent[i]

        # Precompute all ancestors
        for i in range(n):
            for j in range(1, m):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        # time O(logn)
        while k > 0 and node != -1:
            j = int(log2(k))  # Find the largest power of 2 ≤ k
            node = self.dp[node][j]
            k -= (1 << j)  # Subtract the corresponding power of 2

        return node
