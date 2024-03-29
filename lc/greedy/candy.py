from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        # complexity O(n), mem O(n)
        n = len(ratings)
        candy = [1] * n
        for i in range(n - 1):
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i + 1] + 1
            elif ratings[i] < ratings[i + 1] and candy[i] >= candy[i + 1]:
                candy[i + 1] = candy[i] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1] and candy[i] >= candy[i - 1]:
                candy[i - 1] = candy[i] + 1
        return sum(candy)
