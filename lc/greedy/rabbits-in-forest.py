class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # hashmap greedy
        # Time O(N), space O(N)
        cnt = Counter(answers)
        return sum(math.ceil(cnt[k] / (k+1)) * (k+1) for k in cnt)
