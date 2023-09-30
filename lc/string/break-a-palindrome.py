class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        for i in range(len(palindrome) // 2):
            if ord(palindrome[i]) - ord('a') > 0:
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:len(palindrome)-1] + 'b'


s = Solution()
print(s.breakPalindrome('abccba'))
print(s.breakPalindrome('aaaaaa'))
