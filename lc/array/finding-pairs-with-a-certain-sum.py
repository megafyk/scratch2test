class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freq = defaultdict(int)
        self.nums1 = nums1
        self.nums2 = nums2
        for num in nums2:
            self.freq[num] += 1
            

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        new_num = num + val
        self.nums2[index] = new_num
        self.freq[num] -= 1
        if self.freq[num] == 0:
            del self.freq[num]
        self.freq[new_num] += 1

        

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums1:
            t = tot - num
            cnt += self.freq[t]
        return cnt

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)