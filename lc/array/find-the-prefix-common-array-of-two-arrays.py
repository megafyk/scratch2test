class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # arr + hashmap
        # time O(N), space O(N)

        hA = set()
        hB = set()
        n = len(A)
        C = [0] * n
        cnt = 0
        for i in range(n):
            a, b = A[i], B[i]
            hA.add(a)
            hB.add(b)
            if a in hB:
                cnt += 1
            if b in hA:
                cnt += 1
            if a == b:
                cnt -= 1
            C[i] = cnt
        return C
