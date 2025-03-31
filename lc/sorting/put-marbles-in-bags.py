class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # greedy + sorting
        # time O(NlogN), space O(N)
        if k == 1: return 0

        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i + 1])

        splits = sorted(splits)

        t = k - 1
        max_score = sum(splits[-t:])
        min_score = sum(splits[:t])
        return max_score - min_score
