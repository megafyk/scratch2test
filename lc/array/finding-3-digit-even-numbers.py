class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # array
        # time O(n^3), space O(1)
        n = len(digits)
        res = set()
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or k == i:
                        continue
                    if digits[k] % 2 == 1:
                        continue
                    
                    res.add(100 * digits[i] + 10 * digits[j] + digits[k])
        
        return sorted(list(res))
 