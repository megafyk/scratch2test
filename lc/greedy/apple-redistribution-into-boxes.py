class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        i = j = 0
        cur = capacity[0]

        while i < len(apple):
            if apple[i] <= cur:
                cur -= apple[i]
                i += 1
            else:
                apple[i] -= cur
                j += 1
                cur = capacity[j]
        return j + 1