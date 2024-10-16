class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy
        # time O(nlogn), space O(1)
        arr = ["", ""]

        pq = []
        if a > 0:
            heappush(pq, (-a, "a"))
        if b > 0:
            heappush(pq, (-b, "b"))
        if c > 0:
            heappush(pq, (-c, "c"))

        while pq:
            remain, ch = heappop(pq)
            if arr[-1] == arr[-2] == ch:
                if not pq:
                    break
                r, c = heappop(pq)
                r += 1
                arr.append(c)
                if r != 0:
                    heappush(pq, (r, c))
                heappush(pq, (remain, ch))
            else:
                remain += 1
                arr.append(ch)
                if remain != 0:
                    heappush(pq, (remain, ch))

        return "".join(arr)


# class Solution:

#     def backtrack(self,a,b,c,cur):
#         n = len(cur)
#         mx_str = cur
#         if a > 0 and (n < 2 or (n >= 2 and cur[-2:] != "aa")):
#             add_a = self.backtrack(a-1,b,c,cur+"a")
#             if len(add_a) > len(mx_str): mx_str = add_a
#         if b > 0 and (n < 2 or (n >= 2 and cur[-2:] != "bb")):
#             add_b = self.backtrack(a,b-1,c,cur+"b")
#             if len(add_b) > len(mx_str): mx_str = add_b
#         if c > 0 and (n < 2 or (n >= 2 and cur[-2:] != "cc")):
#             add_c = self.backtrack(a,b,c-1,cur+"c")
#             if len(add_c) > len(mx_str): mx_str = add_c
#         return mx_str
        
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         return self.backtrack(a,b,c, "")
