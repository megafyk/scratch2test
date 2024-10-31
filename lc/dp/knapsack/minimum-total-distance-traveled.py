class Solution:
    def mincost(self, robot, factory, robot_pos, factory_pos, memo):
        if robot_pos < 0: return 0
        if factory_pos < 0: return sys.maxsize
        if (robot_pos, factory_pos) in memo: return memo[(robot_pos, factory_pos)]
        # choose fix
        fix = abs(robot[robot_pos] - factory[factory_pos]) + self.mincost(robot, factory, robot_pos-1, factory_pos-1, memo)
        not_fix = self.mincost(robot, factory, robot_pos, factory_pos-1, memo)
        memo[(robot_pos, factory_pos)] = min(fix,not_fix)
        return memo[(robot_pos, factory_pos)]

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # dp knapsack 0/1
        # time O(m*n), space (m*n)
        robot = sorted(robot)
        factory = sorted(factory)
        nw_factory = []
        for pos,cnt in factory:
            nw_factory += [pos] * cnt
        memo = {}
        return self.mincost(robot, nw_factory, len(robot)-1, len(nw_factory)-1, memo)
