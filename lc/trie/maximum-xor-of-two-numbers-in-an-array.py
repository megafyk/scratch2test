class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.isnum = False

class Solution:
    def insert(self, root, num, bin_max_num):
        curr = root
        bnum = bin(num)[2:]
        bnum = '0' * (len(bin_max_num) - len(bnum)) + bnum
        for i in range(len(bnum)):
            bit = int(bnum[i])
            if not curr.child[bit]:
                curr.child[bit] = TrieNode()
            curr = curr.child[bit]
        curr.isnum = True
    
    def find_max_xor(self, root, num, bin_max_num):
        curr = root
        bnum = bin(num)[2:]
        bnum = '0' * (len(bin_max_num) - len(bnum)) + bnum
        res = 0
        for i in range(len(bnum)):
            bit = int(bnum[i])
            toggle_bit = bit ^ 1
            if curr.child[toggle_bit]:
                res = res << 1 | toggle_bit
                curr = curr.child[toggle_bit]
            else:
                res = res << 1 | bit
                curr = curr.child[bit]
        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        # complexity O(nlogk), mem O(nlogk), k = len(max(nums))
        root = TrieNode()
        max_num = max(nums)
        bin_max_num = bin(max_num)[2:]
        for num in nums:
            self.insert(root, num, bin_max_num)
        res = 0

        for num in nums:
            res = max(res, num ^ self.find_max_xor(root, num, bin_max_num))
        return res