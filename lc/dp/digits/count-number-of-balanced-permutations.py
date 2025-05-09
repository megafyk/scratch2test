class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # dp combinatoric
        # time O(total*digits), space (total * digits)
        n = len(num)
        mod = 10 ** 9 + 7
        total_d = sum([int(d) for d in num])

        if total_d % 2 == 1: return 0
        # preprocessing factorial
        fact = [1] * (n+1)
        for i in range(1, n+1): 
            fact[i] = (fact[i-1] * i) % mod
        inv = [1] * (n+1)
        for i in range(2, n+1):
            inv[i] = mod - (mod // i) * inv[mod%i] % mod # euclid formula
        inv_fact = [1] * (n+1)
        for i in range(1, n+1):
            inv_fact[i] = (inv_fact[i-1] * inv[i]) % mod
        

        half_total = total_d // 2
        half_num = n // 2
        # dp[i][j] => num of ways with sum=i use j digits
        dp = [[0] * (half_num + 1) for _ in range(half_total+1)]
        dp[0][0] = 1
        cnt = defaultdict(int)
        for d in num:
            d = int(d)
            cnt[d] += 1
            # inverse loop => a digit must be use once
            for i in range(half_total, d-1, -1):
                for j in range(half_num, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i-d][j-1]) % mod

        res = (dp[-1][-1] * fact[half_num] * fact[n-half_num]) % mod

        # remove duplicate digits from permutation
        for v in cnt.values():
            res = (res * inv_fact[v]) % mod
        return res % mod