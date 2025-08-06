
class Solution1:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # segment tree
        # time O(nlogb), space O(4*b)
        b = len(baskets)
        st_size = 4 * b 
        st = [0] * st_size

        def build(node, l, r):
            if l == r:
                st[node] = baskets[l]
                return
            m = (l + r) // 2
            build(2 * node, l, m)
            build(2 * node + 1, m + 1, r)
            st[node] = max(st[2 * node], st[2 * node + 1])

        build(1, 0, b - 1)

        def find_and_update(node, l, r, fruit):
            if st[node] < fruit:
                return -1
            if l == r:
                st[node] = -1
                return l
            m = (l + r) // 2
            found = find_and_update(2 * node, l, m, fruit)
            if found == -1:
                found = find_and_update(2 * node + 1, m + 1, r, fruit)
            st[node] = max(st[2 * node], st[2 * node + 1]) 
            return found

        res = 0
        for fruit in fruits:
            if find_and_update(1, 0, b - 1, fruit) == -1:
                res += 1
        return res

class Solution1:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # tle
        # log(nsqrt(b)), space O(sqrt(b))
        n = len(baskets)
        size = int(n**(1/2))
        group_cnt = (n+size) // size
        groups = [0] * group_cnt
        for i in range(n):
            groups[i//size] = max(groups[i//size], baskets[i])
        res = 0
        for fruit in fruits:
            used = False
            for i in range(len(groups)):
                if fruit > groups[i]: continue
                groups[i] = 0
                pos = i * size
                for j in range(pos, min(n, pos+size)):
                    if baskets[j] >= fruit and not used:
                        baskets[j] = 0
                        used = True
                    groups[i] = max(groups[i], baskets[j])
            if not used: res += 1
        return res
