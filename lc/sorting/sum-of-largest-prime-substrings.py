class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        # sorting + prime
        # time O(n^2 * log(n) + n^2log(n^2)), space O(n^2)
        def is_prime(n):
            if n == 1: return False
            if n == 2: return True
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        primes = set()
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                num = int(s[i:j+1])
                
                if is_prime(num):
                    primes.add(num)

        primes = sorted(primes, reverse=True)
        total = 0
        for i in range(min(3, len(primes))):
            total += primes[i]
        return total
                