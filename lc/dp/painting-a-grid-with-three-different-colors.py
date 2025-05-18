class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # dp bitmask
        # time O(3^m*m + 3^2m*m + n*3^m) = O(9^m*m+n*3^m), space O(3^m + n*3^m)
        mod = 10 ** 9 + 7

        valid = defaultdict(list)
        for key in range(3**m): # bitmask base3: red,green,blue => 0,1,2
            row = []
            mask = key
            for i in range(m):
                row.append(mask % 3)
                mask //= 3
            if not any(row[i-1] == row[i] for i in range(1,m)):
                # a valid row
                valid[key] = row
        
       
        adj_valid = defaultdict(list)
        for mask1,row1 in valid.items():
            for mask2,row2 in valid.items():
                # combination of valid row2 to row1
                if not any(row1[i] == row2[i] for i in range(m)):
                    adj_valid[mask1].append(mask2)
        
        @cache
        def dp(i,mask):
            if i == n-1: return 1
            count = 0
            for valid in adj_valid[mask]:
                count = (count + dp(i+1, valid)) % mod
            return count
        
        res = 0
        for mask in valid.keys():
            res = (res + dp(0,mask)) % mod
        return res % mod