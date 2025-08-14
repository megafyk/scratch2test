class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # sliding window
        # time O(log(num)), space O(log(num))
        res = ""
        mx = -1
        num_str = str(num)
        for i in range(len(num_str)):
            if i >= 2:
                if num_str[i] == num_str[i-1] == num_str[i-2]:
                    t = int(num_str[i-2: i+1])
                    if t > mx:
                        mx = t
                        res = num_str[i-2: i+1]
        return res