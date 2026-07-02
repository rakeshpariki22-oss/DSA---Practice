import heapq
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dis = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq = [(grid[0][0], 0, 0)]
        
        while pq:
            val, cx, cy = heapq.heappop(pq)
            
            # Early exit: if we pop the destination, check if cost < health
            if cx == m - 1 and cy == n - 1:
                return val < health
                
            if dis[cx][cy] >= 0:
                continue
                
            dis[cx][cy] = val
            
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and dis[nx][ny] == -1:
                    heapq.heappush(pq, (val + grid[nx][ny], nx, ny))
                    
        return False