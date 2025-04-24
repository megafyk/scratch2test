class Solution:
    def countLargestGroup(self, n: int) -> int:
        # hashmap
        # time O(NlogM), space O(N)
        freq = defaultdict(int)
        for num in range(1, n+1):
            sum_d = sum([int(d) for d in str(num)])
            freq[sum_d] += 1

        freq_size = defaultdict(int)
        max_size = 0
        res = 0

        for v in freq.values():
            freq_size[v] += 1
            max_size = max(max_size, v)
        return freq_size[max_size]