class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.isnum = False
        self.cnt = 0

class Solution:
    def insert(self, root, num, bin_max_num):
        curr = root
        bnum = bin(num)[2:]
        bnum = '0' * (len(bin_max_num) - len(bnum)) + bnum
        for i in range(len(bnum)):
            bit = int(bnum[i])
            if not curr.child[bit]:
                curr.child[bit] = TrieNode()
            curr.child[bit].cnt += 1   
            curr = curr.child[bit]
        curr.isnum = True
    
    def remove(self, root, num, bin_max_num):
        curr = root
        bnum = bin(num)[2:]
        bnum = '0' * (len(bin_max_num) - len(bnum)) + bnum
        for i in range(len(bnum)):
            bit = int(bnum[i])
            curr.child[bit].cnt -= 1
            curr = curr.child[bit]
        curr.isnum = False

    def find_max_xor(self, root, num, bin_max_num):
        curr = root
        bnum = bin(num)[2:]
        bnum = '0' * (len(bin_max_num) - len(bnum)) + bnum
        res = 0
        for i in range(len(bnum)):
            bit = int(bnum[i])
            toggle_bit = bit ^ 1
            if curr.child[toggle_bit] and curr.child[toggle_bit].cnt > 0:
                res = res << 1 | toggle_bit
                curr = curr.child[toggle_bit]
            else:
                res = res << 1 | bit
                curr = curr.child[bit]
        return res
        
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        root = TrieNode()
        nums = sorted(nums)
        max_num = nums[-1]
        bin_max_num = bin(max_num)[2:]
        j = 0
        res = 0
        for i, num in enumerate(nums):
            while j < len(nums) and 2 * num >= nums[j]:
                self.insert(root, nums[j], bin_max_num)
                j+=1
            res = max(res, num ^ self.find_max_xor(root, num, bin_max_num))
            self.remove(root, num, bin_max_num)
        return res