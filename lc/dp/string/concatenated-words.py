class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # dp string
        # time O(n*L^3), space O(n) 
        words = set(words)
        res = []

        @cache
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in words and suffix in words) or (
                    prefix in words and dfs(suffix)
                ):
                    return True
            return False

        for word in words:
            if dfs(word):
                res.append(word)

        return res
