class Solution:
    def transform(self, n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total
        
    def convert(self, s):
        return ''.join([str((ord(ch) - ord('a') + 1)) for ch in s])

    def getLucky(self, s: str, k: int) -> int:
        convert = self.convert(s)
        convert = int(convert)
        for _ in range(k):
            convert = self.transform(convert)
        return convert
