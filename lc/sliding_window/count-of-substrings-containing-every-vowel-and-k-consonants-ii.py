class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # sliding window
        # time O(N), space O(1)
        def atleast_k(k):
            vowels = defaultdict(int)
            res = 0
            cnt_cons = 0
            i = 0
            for j in range(len(word)):
                c = word[j]
                if c in "aeiou":
                    vowels[c] += 1
                else:
                    cnt_cons += 1

                while len(vowels) == 5 and cnt_cons >= k:
                    res += (len(word) - j)
                    if word[i] in "aeiou":
                        vowels[word[i]] -= 1
                    else:
                        cnt_cons -= 1
                    if vowels[word[i]] == 0:
                        vowels.pop(word[i])
                    i += 1

            return res

        return atleast_k(k) - atleast_k(k+1)