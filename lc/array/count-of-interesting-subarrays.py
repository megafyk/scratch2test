class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1
        res = 0
        for num in nums:
            prefix += 1 if num % modulo == k else 0
            res += freq[(prefix - k + modulo) % modulo]
            freq[prefix % modulo] += 1
        return res