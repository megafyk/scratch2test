class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # sliding window
        # time O(N), space O(N)
        N = len(nums)
        k = len(set(nums))
        freq = defaultdict(int)
        res = 0
        i = 0
        for j in range(N):
            freq[nums[j]] += 1
            while len(freq) == k:
                res += N-j
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del(freq[nums[i]])
                i += 1
        return res