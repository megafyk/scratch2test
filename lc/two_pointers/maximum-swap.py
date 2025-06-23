
class Solution:
    def maximumSwap(self, num: int) -> int:
        # 2 pointers
        # time O(n), space O(n) 
        arr = list(str(num))
        mx_d = "0"
        mx_i = -1
        swap_i = swap_j = -1
        for i in reversed(range(len(arr))):
            if arr[i] > mx_d:
                mx_d = arr[i]
                mx_i = i
            if arr[i] < mx_d:
                swap_i, swap_j = i, mx_i
        
        arr[swap_i], arr[swap_j] = arr[swap_j], arr[swap_i]
        return int(''.join(arr))
    
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         # brute force
#         # time O(n^2), space O(n)
#         s = list(str(num))
#         mx = num
#         for i in range(len(s)-1):
#             for j in range(i+1, len(s)):
#                 if s[i] < s[j]:
#                     s[i], s[j] = s[j],s[i]
#                     mx = max(mx, int(''.join(s)))
#                     s[i], s[j] = s[j],s[i]
#         return mx