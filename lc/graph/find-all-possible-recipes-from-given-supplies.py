class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # toposort 
        # time O(n), space O(n)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)
            for ing in ingredient:
                graph[ing].append(recipe)
        
        q = deque(supplies)
        s = set(recipes)
        res = []
        while q:
            supply = q.popleft()
            if supply in s:
                res.append(supply)

            for recipe in graph[supply]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)
            
        return res