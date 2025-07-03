class Solution:
    def kthCharacter(self, k: int) -> str:
        # s = "a"
        # while len(s) < k:
        #     for i in range(len(s)):
        #         if s[i] == 'z':
        #             s += 'a'
        #         else:
        #             s += chr(ord(s[i]) + 1)
        # return s[k-1]
        # math
        # time O(log(k)),space O(1)
        return  chr(ord("a") + (k-1).bit_count()) # count bit (k-1) == number of time shift 'a'