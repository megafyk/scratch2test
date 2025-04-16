class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # sliding window
        # time O(N), space O(N)
        N = len(nums)
        cur_freq = defaultdict(int)
        i = 0
        res = 0
        cur_pairs = 0
        for j in range(N):
            cur_pairs += cur_freq[nums[j]]
            cur_freq[nums[j]] += 1
            while cur_pairs >= k:
                cur_freq[nums[i]] -= 1
                cur_pairs -= cur_freq[nums[i]]
                i += 1
            res += i
        return res