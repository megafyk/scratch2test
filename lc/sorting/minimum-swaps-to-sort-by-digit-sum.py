from functools import cmp_to_key

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # sorting + array
        # time O(d*n + nlogn + n) = O(d*n + nlogn), space O(n+n) = O(n)
        sum_d = defaultdict(int)

        def get_sum_d(num):
            return sum(int(d) for d in str(num))
        
        for num in nums:
            sum_d[num] = get_sum_d(num)    

        def cmp(x,y):
            a,b = x[0], y[0]
            t1 = sum_d[a]
            t2 = sum_d[b]
            if t1 > t2: return 1
            elif t1 < t2: return -1
            else: 
                if a > b: return 1
                else: return -1
        
        nums_with_idx = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_idx = sorted(nums_with_idx,key=cmp_to_key(cmp))

        cnt = 0

        for i in range(len(nums)):
            while i != nums_with_idx[i][1]:
                idx = nums_with_idx[i][1]
                nums_with_idx[i], nums_with_idx[idx] = nums_with_idx[idx], nums_with_idx[i]
                cnt += 1

        return cnt