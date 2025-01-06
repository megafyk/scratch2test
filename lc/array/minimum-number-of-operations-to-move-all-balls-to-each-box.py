class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # array prefix sum
        # time O(n), space O(n)
        n = len(boxes)

        l=0
        r=0
        cnt_l = 0
        cnt_r = 0

        res = [0] * n
        for i in range(n):
            # left pass
            res[i] += l
            cnt_l += 1 if boxes[i] == "1" else 0
            l += cnt_l
            
            # right pass
            j = n-i-1
            res[j] += r
            cnt_r += 1 if boxes[j] == "1" else 0
            r += cnt_r
        return res
            
