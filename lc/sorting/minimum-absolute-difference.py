class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        mi = sys.maxsize

        for i in range(n-1):
            mi = min(mi, abs(arr[i] - arr[i+1]))

        pairs = []
        for i in range(n-1):
            if abs(arr[i] - arr[i+1]) == mi:
                pairs.append([arr[i], arr[i+1]])
                
        return pairs