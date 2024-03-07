from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        pre_degree = [0 for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            # neighbors of a course
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            # courses must finished before go on
            pre_degree[prerequisites[i][0]] += 1
        # add all node with no parent to queue
        q = deque([i for i in range(len(pre_degree)) if pre_degree[i] == 0])
        
        while q:
            course = q.popleft()
            for next_course in graph[course]:
                pre_degree[next_course] -= 1
                if pre_degree[next_course] == 0:
                    q.append(next_course)
        
        return all(degree == 0 for degree in pre_degree)
