class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # matrix
        # time O(n^2+log(n^2)), space O(n)
        n = len(grid)

        for i in range(n):
            x,y = i,0
            arr = []
            while x < n:
                arr.append(grid[x][y])
                x,y = x+1,y+1
            arr.sort(reverse=True)

            x,y = i,0
            j = 0
            while j < len(arr):
                grid[x][y] = arr[j]
                x,y = x+1,y+1
                j += 1

        for i in range(n):
            x,y = 0,i+1
            arr = []
            while y < n:
                arr.append(grid[x][y])
                x,y = x+1,y+1
            arr.sort()
            x,y = 0,i+1
            j = 0
            while j < len(arr):
                grid[x][y] = arr[j]
                x,y = x+1,y+1
                j+=1
                
        return grid