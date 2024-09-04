class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # simulation
        # complexity: time O(n), mem O(1)
        cur_x, cur_y = 0, 0
        cur_dir_x, cur_dir_y = 0, 1

        obs = defaultdict(list)
        for x, y in obstacles:
            obs[(x, y)] = 1
        mx = 0
        for cmd in commands:
            if cmd == -1:
                cur_dir_x, cur_dir_y = cur_dir_y, -cur_dir_x # rotate right 90 (x,y) -> (y,-x)
            elif cmd == -2:
                cur_dir_x, cur_dir_y = -cur_dir_y, cur_dir_x # rotate left 90 (x,y) -> (-y, x)
            else:
                while cmd > 0:
                    tmpx, tmpy = cur_x + cur_dir_x, cur_y + cur_dir_y
                    if (tmpx, tmpy) in obs:
                        break 
                    cur_x, cur_y = tmpx, tmpy
                    mx = max(mx, cur_x**2 + cur_y**2)
                    cmd -= 1
        return mx
