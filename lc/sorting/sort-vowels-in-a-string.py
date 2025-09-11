class Solution:
    def sortVowels(self, s: str) -> str:
        # counting sort
        # time O(n), space O(1)
        vowels_set = {'A','E','I','O','U','a','e','i','o','u'}
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        order = defaultdict(int)
        t = []
        for c in s:
            if c in vowels_set:
                order[c] += 1
            t.append(c)

        for j in range(len(t)):
            if t[j] in vowels_set:
                for v in vowels:
                    if order[v] > 0:
                        t[j] = v
                        order[v] -= 1
                        break
                    
        
        return ''.join(t)