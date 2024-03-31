class Solution:
    # complexity O(n), mem O(1)
    # def valid_after_remove(self, s, first, last, remove):
    #     while first <= last:
    #         if s[first] != s[last]:
    #             if remove == 0:
    #                 return False
    #             else:
    #                 return self.valid_after_remove(
    #                     s, first + 1, last, remove - 1
    #                 ) or self.valid_after_remove(s, first, last - 1, remove -1)
    #         first += 1
    #         last -= 1
    #     return True

    # def validPalindrome(self, s: str) -> bool:
    #     first = 0
    #     last = len(s) - 1
    #     return self.valid_after_remove(s, first, last, 1)

    # complexity O(n), mem O(1)
    def validPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        while first <= last:
            if s[first] != s[last]:
                return (
                    s[first:last] == s[first:last][::-1]
                    or s[first + 1 : last + 1] == s[first + 1 : last + 1][::-1]
                )
            else:
                first += 1
                last -= 1
        return True
