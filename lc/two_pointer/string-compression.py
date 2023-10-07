from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        start, pos = 0, 0
        for i in range(len(chars)):
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                chars[pos] = chars[i]
                pos += 1
                if i > start:
                    for c in str(i - start + 1):
                        chars[pos] = c
                        pos += 1

                start = i + 1
        return pos


s = Solution()
print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
