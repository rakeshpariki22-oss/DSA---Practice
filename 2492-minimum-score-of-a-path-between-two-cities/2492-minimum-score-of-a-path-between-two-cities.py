class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        
        adj = defaultdict(list) # node -> list of (nei, dist)
        
        # Fixed typo: changed 'scr' to 'src'
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))
            
        res = float("inf")
        visit = set()
        
        # Properly indented inside minScore
        def dfs(i):
            nonlocal res # Allows us to modify 'res' from the outer function
            
            if i in visit:
                return
            
            visit.add(i)
            
            for nei, dist in adj[i]:
                res = min(res, dist)
                dfs(nei)
                
        dfs(1)
        
        # Make sure return is inside minScore as well
        return int(res)