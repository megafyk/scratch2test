import bisect

class TimeMap:
    
    def __init__(self):
        # time O(k*t)    
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # time O(NlogN), space O(N)
        bisect.insort_right(self.data[key], (timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # time O(logN), space O(1)
        if key not in self.data: return ""
        left, right = 0, len(self.data[key]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.data[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if left == 0: return ""
        if left == len(self.data[key]):
            return self.data[key][-1][1]
        return self.data[key][left-1][1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)