class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # bitwise
        # time O(n), space O(1)
        cnt_prime_set_bits = 0
        primes = {2,3,5,7,11,13,17,19}

        for num in range(left, right+1):
            if num.bit_count() in primes:
                cnt_prime_set_bits += 1
        return cnt_prime_set_bits