class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 2: return True
            if num % 2 == 0 or num == 1: return False
            for i in range(3, int(math.sqrt(num)+1)):
                if num % i == 0:
                    return False
            return True
        primes = []
        for num in range(left, right + 1):
            if is_prime(num):
                if primes and num <= primes[-1] + 2:
                    return [primes[-1], num]
                primes.append(num)

        res = [-1, -1]
        
        if len(primes) <= 1: return res
        min_diff = 10**6

        for i in range(len(primes)-1):
            diff = primes[i+1] - primes[i]
            if diff < min_diff:
                res[0] = primes[i]
                res[1] = primes[i+1]
                min_diff = diff
        return res