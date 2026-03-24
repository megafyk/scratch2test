class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def get_sum(self, p):
        idx = p + 1
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= (idx & (-idx))
        return ans
    
    def update(self, p, v):
        idx = p + 1
        while idx <= self.n:
            self.bit[idx] += v
            idx += (idx & (-idx))

def main():
    arr = [8,4,1,24,6,9,10] 
    tree = FenwickTree(len(arr))
    for i, num in enumerate(arr):
        tree.update(i, num)
    print(tree.get_sum(6))
    print(tree.get_sum(2))
    tree.update(2, 3-arr[2])
    print(tree.get_sum(2))

if __name__ == "__main__":
    main()
        