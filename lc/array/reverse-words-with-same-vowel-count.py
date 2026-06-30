class Solution:
    def reverseWords(self, s: str) -> str:
        # array + simulation
        # time O(n), space O(n)
        arr = s.split(" ")

        def cnt_vowels(word):
            cnt = 0
            for c in word:
                if c in "aeiou":
                    cnt += 1
            return cnt

        cnt_word0 = cnt_vowels(arr[0])

        for i in range(1, len(arr)):
            cnt_word = cnt_vowels(arr[i])
            if cnt_word0 == cnt_word:
                arr[i] = arr[i][::-1]

        return " ".join(arr)
