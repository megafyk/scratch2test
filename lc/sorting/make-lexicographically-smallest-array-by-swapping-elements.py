class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # sorting with deque -> group element with limit and pickup
        # time O(nlogn), space O(n)
        groups = []
        num_to_group = {}
        for n in sorted(nums):
            if not groups or abs(groups[-1][-1] - n) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) - 1

        res = []
        for n in nums:
            gr = groups[num_to_group[n]]
            res.append(gr.popleft())
        return res
