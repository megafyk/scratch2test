class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # optimize from brute force
        # time O(k*(m+n)), space O(m+n)
        def rotate(fr_m, to_m, fr_n, to_n):
            a = to_m - fr_m + 1
            b = to_n - fr_n + 1
            if a <= 1 or b <= 1:
                return False
            l = k % (2 * (a + b) - 4)
            arr = []
            for j in range(fr_n, to_n):
                arr.append(grid[fr_m][j])

            for i in range(fr_m, to_m):
                arr.append(grid[i][to_n])

            for j in range(to_n, fr_n, -1):
                arr.append(grid[to_m][j])

            for i in range(to_m, fr_m, -1):
                arr.append(grid[i][fr_n])

            arr = arr[l:] + arr[:l]
            idx = 0
            for j in range(fr_n, to_n):
                grid[fr_m][j] = arr[idx]
                idx += 1

            for i in range(fr_m, to_m):
                grid[i][to_n] = arr[idx]
                idx += 1

            for j in range(to_n, fr_n, -1):
                grid[to_m][j] = arr[idx]
                idx += 1

            for i in range(to_m, fr_m, -1):
                grid[i][fr_n] = arr[idx]
                idx += 1

            return True

        m, n = len(grid), len(grid[0])
        fr_m, to_m, fr_n, to_n = 0, m - 1, 0, n - 1
        while True:
            rotated = rotate(fr_m, to_m, fr_n, to_n)
            if not rotated:
                break
            fr_m += 1
            to_m -= 1
            fr_n += 1
            to_n -= 1

        return grid


class Solution1:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # brute force
        # time O(k*(m^2 + n^2)), space O(1)
        def rotate(fr_m, to_m, fr_n, to_n):
            a = to_m - fr_m + 1
            b = to_n - fr_n + 1
            if a <= 1 or b <= 1:
                return False
            step = k % (2 * (a + b) - 4)
            for _ in range(step):
                tmp = grid[fr_m][fr_n]
                for j in range(fr_n, to_n):
                    grid[fr_m][j] = grid[fr_m][j + 1]
                for i in range(fr_m, to_m):
                    grid[i][to_n] = grid[i + 1][to_n]
                for j in range(to_n, fr_n, -1):
                    grid[to_m][j] = grid[to_m][j - 1]
                for i in range(to_m, fr_m, -1):
                    grid[i][fr_n] = grid[i - 1][fr_n]
                grid[fr_m + 1][fr_n] = tmp
            return True

        m, n = len(grid), len(grid[0])
        fr_m, to_m, fr_n, to_n = 0, m - 1, 0, n - 1
        while True:
            rotated = rotate(fr_m, to_m, fr_n, to_n)
            if not rotated:
                break
            fr_m += 1
            to_m -= 1
            fr_n += 1
            to_n -= 1

        return grid
