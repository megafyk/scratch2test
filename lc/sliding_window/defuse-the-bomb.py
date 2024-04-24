class Solution:
    def pos(self, i, n):
        return i % n 

    def decrypt(self, code: List[int], k: int) -> List[int]:
        # complexity: time O(n), mem O(n)
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        elif k > 0:
            begin,end = 1,0
        else:
            k = -k 
            begin,end = n-k, n-k-1
        cur_sum = 0
        tmp = k
        
        while tmp > 0:
            tmp -= 1
            end = self.pos(end+1, n)
            cur_sum += code[end]

        for i in range(n):
            res[i] = cur_sum
            end = self.pos(end+1, n)
            cur_sum = cur_sum + code[end] - code[begin]
            begin = self.pos(begin+1, n)
        return res
            
        