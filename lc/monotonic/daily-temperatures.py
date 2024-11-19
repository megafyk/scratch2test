from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # complexity: time O(n), mem O(n)
        stack = deque()
        n = len(temperatures)
        res = [0] * n
        i = 0
        
        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res