class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # dp
        # complexity: time O(n*w), mem O(n)
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # if book i belongs new shelf
            w, h = books[i - 1]
            dp[i] = dp[i - 1] + h

            # if book i belongs old shelf
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + h)

        return dp[-1]
