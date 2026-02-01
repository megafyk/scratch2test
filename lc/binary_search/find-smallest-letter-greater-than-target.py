class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search
        # n = len(letters)
        # time O(logn), space O(1)
        idx = bisect.bisect_right(letters, target)
        if idx == len(letters):
            return letters[0]
        return letters[idx]