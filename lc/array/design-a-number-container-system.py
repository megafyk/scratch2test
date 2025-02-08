class NumberContainers:

    def __init__(self):
        self.idx_to_num = {}
        self.num_to_idx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            cur_num = self.idx_to_num[index]
            arr = self.num_to_idx[cur_num]
            del_idx = bisect.bisect_left(arr, index)
            arr.pop(del_idx)

        self.idx_to_num[index] = number
        bisect.insort(self.num_to_idx[number], index)


    def find(self, number: int) -> int:
        if number in self.num_to_idx and len(self.num_to_idx[number]) > 0:
            return self.num_to_idx[number][0]
        return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
