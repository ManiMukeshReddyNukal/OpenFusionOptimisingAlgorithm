from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        
        rows, cols = len(rooms), len(rooms[0])
        gates = deque()
        
        # Step 1: initialize the queue with all gates' positions
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        
        # Step 2: BFS from the gates to compute the shortest distance to each room
        while gates:
            row, col = gates.popleft()
            
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r, c = row + dr, col + dc
                # Proceed if it's a valid room and hasn't been visited yet (rooms[r][c] is INF)
                if 0 <= r < rows and 0 <= c < cols and  (rooms[r][c] == 2147483647):
                    rooms[r][c] = rooms[row][col] + 1  # Update distance to gate
                    gates.append((r, c))  # Add new room position to queue

