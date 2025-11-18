class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        m = len(people)
        req_skills_map = {}
        
        for i, skill in enumerate(req_skills):
            req_skills_map[skill] = i

        def update(mask, skills):
            for skill in skills:
                i = req_skills_map[skill]
                mask |= (1 << i)
            return mask

        q = deque([(0, 0)])
        visit = set()
        visit.add(0)

        pick = 0
        while q:
            mask, mask_p = q.popleft()
            if mask == ((1 << n) - 1):
                pick = mask_p
                break

            for i in range(m):
                if (mask_p >> i) & 1 == 0:
                    nw_mask_p = mask_p | (1 << i)
                    nw_mask = update(mask, people[i])
                    if nw_mask not in visit:
                        visit.add(nw_mask)
                        q.append((nw_mask, nw_mask_p))
        res = []
        for i in range(m):
            if (pick >> i) & 1 == 1:
                res.append(i)
        return res