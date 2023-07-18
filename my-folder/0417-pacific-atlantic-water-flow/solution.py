class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        # Create visited matrices for both oceans
        pacific_visited = [[False] * cols for _ in range(rows)]
        atlantic_visited = [[False] * cols for _ in range(rows)]
        
        # Create queue for both oceans
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Add cells in the first and last rows to their respective queues
        for col in range(cols):
            pacific_queue.append((0, col))
            atlantic_queue.append((rows-1, col))
            pacific_visited[0][col] = True
            atlantic_visited[rows-1][col] = True
        
        # Add cells in the first and last columns to their respective queues
        for row in range(rows):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols-1))
            pacific_visited[row][0] = True
            atlantic_visited[row][cols-1] = True
        
        # Define helper function to check if a cell can flow to an ocean
        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                # Check adjacent cells
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row + dr, col + dc
                    # Check if cell is within bounds and hasn't been visited yet
                    if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                        # Check if cell can flow to the ocean
                        if heights[r][c] >= heights[row][col]:
                            visited[r][c] = True
                            queue.append((r, c))
        
        # Run BFS on both oceans starting from the boundary cells
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
        
        # Find the cells that can flow to both oceans
        result = []
        for row in range(rows):
            for col in range(cols):
                if pacific_visited[row][col] and atlantic_visited[row][col]:
                    result.append([row, col])
        
        return result
