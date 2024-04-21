class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # complexity: time O(n), mem O(n)
        dic = Counter(nums)
        res = 0
        for k,val in dic.items():
            if k-1 in dic: res = max(res, val+dic[k-1])
            if k+1 in dic: res = max(res, val+dic[k+1])
        return res