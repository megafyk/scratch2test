class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # hashtable
        # time O(n), space O(n)
        cnt = Counter(nums)
        res = 0
        if cnt[1] > 0:
            res = cnt[1] - 1 if cnt[1] % 2 == 0 else cnt[1]
        del cnt[1]
        for k, v in cnt.items():
            length, cur = 0, k
            while cnt[cur] > 1:
                length += 1
                cur *= cur
            res = max(res, ((length + cnt[cur]) << 1) - 1)
        return res
