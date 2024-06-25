class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.cnt = 0


class Solution:

    def __init__(self):
        self.root = TrieNode()

    def ins(self, num):
        node = self.root
        for i in range(15, -1, -1):
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.cnt += 1

    def get_pairs(self, num, limit):
        node = self.root
        pairs = 0
        for i in range(15, -1, -1):
            if not node:
                break
            bit = (num >> i) & 1
            bit_limit = (limit >> i) & 1

            if bit_limit:
                if node.child[bit]:
                    pairs += node.child[bit].cnt
                node = node.child[bit ^ 1]
            else:
                node = node.child[bit]

        return pairs

    def countPairs(self, nums, low, high):
        pairs = 0
        for num in nums:
            pairs += self.get_pairs(num, high + 1) - self.get_pairs(num, low)
            self.ins(num)
        return pairs
