class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # increasing monotonic stack
        # time O(n), space O(n)
        dq = deque()

        for i in range(len(arr)):
            if not dq or dq[-1] < arr[i]:
                dq.append(arr[i])
            else:
                mx = dq[-1]
                while dq and dq[-1] > arr[i]:
                    dq.pop()
                dq.append(mx)
        return len(dq)


    # def maxChunksToSorted(self, arr: List[int]) -> int:
    #     # time O(n), space O(1)
    #     chunks = 0
    #     mx = 0
    #     for i in range(len(arr)):
    #         mx = max(mx, arr[i])
    #         if mx == i:
    #             chunks += 1
    #     return chunks
