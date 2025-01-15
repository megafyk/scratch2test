class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # bitwise string
        # time O(log(n)), space O(1) 

        def isset(n, cur_bit):
            return n & (1 << cur_bit) != 0

        def setbit(n, cur_bit):
            return n | (1 << cur_bit)

        res = 0
        bin2 = bin(num2)[2:]
        cnt = Counter(bin2)
        
        set_bit = 0
        cur_bit = 31

        while set_bit < cnt["1"]:
            if isset(num1, cur_bit) or cnt["1"] - set_bit > cur_bit:
                res = setbit(res, cur_bit)
                set_bit += 1
            cur_bit -= 1
        return res
        
# class Solution:
#     def minimizeXor(self, num1: int, num2: int) -> int:
#         # bitwise string
#         # time O(1), space O(1) 
#         bin1 = bin(num1)[2:]
#         bin2 = bin(num2)[2:]
        
#         cnt = Counter(bin2)

#         res = ["0"] * len(bin1)
#         for i in range(len(bin1)):
#             if bin1[i] == "1" and cnt["1"] > 0:
#                 cnt["1"] -= 1
#                 res[i] = "1"

#         for i in range(len(bin1)-1,-1,-1):
#             if cnt["1"] > 0 and res[i] == "0":
#                 res[i] = "1"
#                 cnt["1"] -= 1

#         return int(cnt["1"] * "1" + ''.join(res), 2)