class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # brute force + math
        # time O(10^(k/2)*logk), space O(1)
        def is_base_k_palin(num):
            base_k = ""
            while num > 0:
                base_k = str(num % k) + base_k
                num //= k
            return base_k == base_k[::-1]

        total = 0
        leng = 1
        while n > 0:
            new_leng = leng * 10  # append 1 digit
            for odd in [1, 0]:  # go odd palindrome first (shorter)
                for i in range(leng, new_leng):
                    if n == 0:
                        break
                    num = str(i)
                    if odd:
                        num = num[:-1] + num[::-1]  # create palindrome len odd
                    else:
                        num = num + num[::-1]  # create palindrome len even
                    num = int(num)
                    if is_base_k_palin(num):
                        total += num
                        n -= 1

            leng = new_leng
        return total
