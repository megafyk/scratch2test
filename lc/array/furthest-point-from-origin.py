class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # counter
        # time O(n), space O(1)
        cnt = Counter(moves)
        if cnt["L"] > cnt["R"]:
            return cnt["L"] - cnt["R"] + cnt["_"]
        return cnt["R"] - cnt["L"] + cnt["_"]
