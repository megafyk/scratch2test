import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # complexity O(nlogn), mem O(n)
        nums = list(zip(nums1, nums2))
        nums = sorted(nums, key=lambda x: x[1], reverse=True)
        
        kth_sm = []
        pre_sum = 0
        res = 0
        for n1, n2 in nums:
            pre_sum += n1
            heapq.heappush(kth_sm, n1)

            if len(kth_sm) == k:
                res = max(res, pre_sum * n2)
                pre_sum -= heapq.heappop(kth_sm)

        return res

    # def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    #     # keep track kth largest element in nums1
    #     k_largest_nums1 = [(-num, idx) for idx, num in enumerate(nums1)]
    #     # keep track min
    #     min_nums2 = []
    #     heapq.heapify(k_largest_nums1)
    #     curr_sum = 0

    #     for _ in range(k):
    #         num, idx = heapq.heappop(k_largest_nums1)
    #         curr_sum += -num
    #         heapq.heappush(min_nums2, (nums2[idx], idx))

    #     num, idx = heapq.heappop(min_nums2)
    #     max_sub_score = curr_sum * num
    #     curr_sum -= nums1[idx]

    #     while k_largest_nums1:
    #         num, idx = heapq.heappop(k_largest_nums1)
    #         curr_sum += -num
    #         heapq.heappush(min_nums2, (nums2[idx], idx))
            
    #         num, idx = heapq.heappop(min_nums2)
    #         max_sub_score = max(max_sub_score, curr_sum * num)
    #         curr_sum -= nums1[idx]

    #     return max_sub_score
            