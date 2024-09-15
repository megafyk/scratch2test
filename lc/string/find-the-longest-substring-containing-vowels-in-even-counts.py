class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # sum prefix + bitmask
        # complexity: time O(n), space O(1)
        n = len(s)
        prefix = [-1] * 32
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mask = 0 
        res = 0
        prefix[0] = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= (1 << vowels[s[i]])  
            if prefix[mask] == -1:
                prefix[mask] = i + 1
            else:
                res = max(res, i + 1 - prefix[mask])
        return res
