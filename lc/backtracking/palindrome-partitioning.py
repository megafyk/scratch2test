class Solution:
    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def dfs(self, res, arr, s):
        if not s and arr:
            res.append(list(arr))
            return
        for i in range(len(s)):
            sub = s[: i + 1]

            is_sub_palindrome = self.is_palindrome(sub)

            if is_sub_palindrome:
                arr.append(sub)
                self.dfs(res, arr, s[i + 1 :])
                arr.pop()

    def partition(self, s: str) -> List[List[str]]:
        # complexity: time O(2^n), mem O(n)
        res = []
        self.dfs(res, [], s)
        return res