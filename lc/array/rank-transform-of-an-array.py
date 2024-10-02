class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # array with sorting
        # complexity: time O(nlogn), space O(n)
        n = len(arr)
        arr = [(num, idx) for idx, num in enumerate(arr)]
        arr = sorted(arr)

        rank = [0] * n
        cur = -sys.maxsize
        cur_rank = 0
        for i in range(n):
            if cur < arr[i][0]:
                cur = arr[i][0]
                cur_rank += 1
            rank[arr[i][1]] = cur_rank
            
        return rank
