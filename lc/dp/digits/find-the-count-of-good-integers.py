class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # dfs digits
        # time O(10^(n//2) * nlogn), space O(N)
        # 1. generate palindrome use dfs
        # 2. count permutation that divisible by k
        # 3. remove duplication
        per = set()

        # preprocess factorial result
        fac = [1] * (n+1) 
        for i in range(2, n+1):
            fac[i] = fac[i-1] * i

        def permutation(freq, n):
            # permutation = n! / (r1! * r2! .. * r3!) (r is freq of a digit) 
            p = fac[n]
            for v in freq.values():
                p //= fac[v]
            return p


        def k_palindrome(s):
            digits = ''.join(sorted(s))
            num_str = ''.join(s)
            
            if digits in per or int(num_str) % k != 0:
                return 0
            
            freq = Counter(digits)
            per.add(digits)
            p = permutation(freq, n)
            p_0 = 0
            if '0' in freq:
                freq['0'] -= 1
                p_0 = permutation(freq, n-1)
            
            return p - p_0

        def dfs(idx, s):
            if idx == (n + 1) // 2:
                return k_palindrome(s)
            
            cnt = 0
            start = 0 if idx > 0 else 1
            for d in range(start, 10):
                s[idx] = s[n-idx-1] = str(d)
                cnt += dfs(idx + 1, s)
            return cnt
        
        s = [''] * n
        return dfs(0, s)