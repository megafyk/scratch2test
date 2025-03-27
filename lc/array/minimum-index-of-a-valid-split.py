class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # array with hashtable
        # time O(N), space O(N)
        n = len(nums)
        freq = defaultdict(int)
        prefix = [0] * len(nums)
        for i in range(n):
            freq[nums[i]] += 1
            prefix[i] = freq[nums[i]]
        
        for i in range(n):
            left = i + 1
            right = n - left

            freq_idx_left = prefix[i]
            freq_idx_right = freq[nums[i]] - freq_idx_left

            if freq_idx_left * 2 > left and freq_idx_right * 2 > right:
                return i

        return -1