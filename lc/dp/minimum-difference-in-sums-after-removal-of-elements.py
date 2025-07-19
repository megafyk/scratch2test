class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # heap
        # time O(nlogn), space O(n)
        n = len(nums) // 3
        cur_max_heap = [-nums[i] for i in range(n)]

        heapify(cur_max_heap)
        cur_min = sum(nums[:n])

        prefix_min = [cur_min]

        for i in range(n, 2 * n):
            t = -heappop(cur_max_heap)
            cur_min -= t
            cur_min += min(t, nums[i])
            heappush(cur_max_heap, -min(t, nums[i]))
            prefix_min.append(cur_min)

        cur_min_heap = [nums[i] for i in range(2 * n, 3 * n)]
        heapify(cur_min_heap)
        cur_max = sum(nums[2 * n :])

        suffix_max = [cur_max]
        for i in range(2 * n - 1, n - 1, -1):
            t = heappop(cur_min_heap)
            cur_max -= t
            cur_max += max(t, nums[i])
            heappush(cur_min_heap, max(t, nums[i]))
            suffix_max.append(cur_max)
        suffix_max = suffix_max[::-1]

        res = sys.maxsize
        for i in range(len(prefix_min)):
            res = min(res, prefix_min[i] - suffix_max[i])
        return res
