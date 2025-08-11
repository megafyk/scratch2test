class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # hashtable
        # time O(1), space (1)
        digits = defaultdict(dict)
        for i in range(32):
            t = 2 ** i
            digits[t] = Counter(str(t))
        
        def check(n_digits, t_digits):
            return n_digits == t_digits

        n_digits = Counter(str(n))
        for k,v in digits.items():
            if check(n_digits, v):
                return True
        return False