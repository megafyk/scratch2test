class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v = [v1, v2]
        self.p = [0,0]
        self.k = 0
    """
    @return: An integer
    """
    def _next(self):
        v = self.v[self.k]
        p = self.p[self.k]
        res = v[p]
        self.p[self.k] += 1
        self.k = (self.k + 1) % len(self.v)
        return res
        
    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        start = self.k
        
        while self.p[self.k] >= len(self.v[self.k]):
            self.k = (self.k + 1) % len(self.v)
            if self.k == start:
                return False

        return True

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result