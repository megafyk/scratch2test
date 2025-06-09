class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # dp knapsack
        # time O(n*k), space O(k)
        buy = [-sys.maxsize] * (
            k + 1
        )  # bought[j] = best profit at bought position by j trans
        sell = [0] * (k + 1)  # sell[j] = best profit at sell position by j trans
        res = [0] * (k + 1)  # res[j] = best profit by j trans

        for p in prices:
            for j in range(
                k, 0, -1
            ):  # reverse because [j] should depend only on the previous state [j-1] from the last iteration.
                res[j] = max(res[j], buy[j - 1] + p, sell[j - 1] - p)
                buy[j - 1] = max(buy[j - 1], res[j - 1] - p)
                sell[j - 1] = max(sell[j - 1], res[j - 1] + p)

        return res[k]
