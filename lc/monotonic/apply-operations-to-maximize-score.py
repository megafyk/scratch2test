class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # monotonic stack + heap 
        N = len(nums)
        MOD = 10 ** 9 + 7
        res = 1
        # preproccess prime score
        scores = []
        for num in nums:
            score = 0
            for f in range(2, int(sqrt(num)) + 1):
                if num % f == 0:
                    score += 1
                    while num % f == 0:
                        num /= f
            if num >= 2: # num is prime
                score += 1
            scores.append(score)

        left_bound = [-1] * N
        right_bound = [N] * N
        stack = []

        for i,s in enumerate(scores):
            while stack and scores[stack[-1]] < s:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        
        pq = [(-n, i) for i,n in enumerate(nums)]
        heapify(pq)

        while k > 0:
            n, index = heappop(pq)
            n = -n

            left_cnt = index - left_bound[index]
            right_cnt = right_bound[index] - index
            count = left_cnt * right_cnt
            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations

        return res % MOD