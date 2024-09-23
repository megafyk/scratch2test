class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # complexity: O(n), mem O(n)
        reversed_s = s[::-1]
        double_s = s + "$" + reversed_s

        j = 0
        n = len(double_s)
        kmp = [0] * n
        for i in range(1, n):
            while j > 0 and double_s[j] != double_s[i]:
                j = kmp[j-1]
            
            if double_s[i] == double_s[j]:
                j+= 1
            kmp[i] = j
                
        longest_palindrome_len = kmp[-1]
        suffix_s = s[longest_palindrome_len:]
        prefix_s = suffix_s[::-1]
        return prefix_s + s

    # def ispal(self, s):
    #     return s == s[::-1]

    # def shortestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if self.ispal(s):
    #         return s
    #     prefix = ""
        
    #     for i in range(n-1, -1, -1):
    #         prefix += s[i]
    #         if self.ispal(prefix + s):
    #             return prefix + s
