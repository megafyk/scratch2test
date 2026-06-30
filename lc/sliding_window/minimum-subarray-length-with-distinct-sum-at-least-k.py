class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        # sliding window + hashtable
        # time O(n), space O(n)
        cnt = defaultdict(int)
        cur_sum = 0
        j = 0
        n = len(nums)
        res = inf
        for i in range(n):
            if nums[i] not in cnt:
                cur_sum += nums[i]

            cnt[nums[i]] += 1
            while j <= i and cur_sum >= k:
                res = min(res, i - j + 1)

                if cnt[nums[j]] == 1:
                    cur_sum -= nums[j]

                cnt[nums[j]] -= 1
                if cnt[nums[j]] == 0:
                    del cnt[nums[j]]
                j += 1
        return res if res != inf else -1
