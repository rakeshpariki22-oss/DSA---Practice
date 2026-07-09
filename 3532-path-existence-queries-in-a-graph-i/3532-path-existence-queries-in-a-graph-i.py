class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Array to store the group ID for each node
        groups = [0] * n
        current_group_id = 0
        
        # Traverse the nodes based on the sorted nums array
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_group_id += 1
            groups[i] = current_group_id
            
        # Answer each query
        return [groups[u] == groups[v] for u, v in queries]
