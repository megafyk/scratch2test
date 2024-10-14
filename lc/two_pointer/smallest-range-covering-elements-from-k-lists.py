class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 2 pointers -> k pointers
        # time O(nlogk), space O(k)
        k = len(nums)

        pq = []
        mx = nums[0][0]

        # init k pointer
        for i in range(k):
            heappush(pq, (nums[i][0], i, 0))
            mx = max(mx, nums[i][0])

        res = [0, 10**5 + 1]
        while True:
            # range includes all between mi and mx
            mi, nums_idx, idx = heappop(pq)
            idx += 1
            if mx-mi < res[1]-res[0]:
                res = [mi, mx]

            if idx == len(nums[nums_idx]):
                break
            # shift mi
            new = nums[nums_idx][idx]
            heappush(pq, (new, nums_idx, idx))
            mx = max(mx, new)

        return res