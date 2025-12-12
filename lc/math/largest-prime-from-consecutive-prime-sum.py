class Solution:
    def largestPrime(self, n: int) -> int:
        if n < 2: return 0
        if n == 2: return 2
        primes = []
        def is_prime(num):
            if num == 1: return False
            if num == 2 or num == 3: return True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        res = 0
        total = 0
        for i in range(2, n):
            if is_prime(i):
                total += i
                if total > n: break
                if (is_prime(total)):
                    res = max(res, total)
        return res