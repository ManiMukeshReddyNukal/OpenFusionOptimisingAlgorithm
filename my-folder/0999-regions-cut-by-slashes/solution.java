import java.util.LinkedList;
import java.util.Queue;

class Solution {

    private static final int[][] DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int regionsBySlashes(String[] grid) {
        int gridSize = grid.length;
        int[][] expandGrid = new int[gridSize * 3][gridSize * 3];

        // Expand the grid based on slashes
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                int baseRow = i * 3;
                int baseCol = j * 3;
                if (grid[i].charAt(j) == '\\') {
                    expandGrid[baseRow][baseCol] = 1;
                    expandGrid[baseRow + 1][baseCol + 1] = 1;
                    expandGrid[baseRow + 2][baseCol + 2] = 1;
                } else if (grid[i].charAt(j) == '/') {
                    expandGrid[baseRow][baseCol + 2] = 1;
                    expandGrid[baseRow + 1][baseCol + 1] = 1;
                    expandGrid[baseRow + 2][baseCol] = 1;
                }
            }
        }

        int regionCount = 0;
        
        // Perform flood fill and count regions
        for (int i = 0; i < gridSize * 3; i++) {
            for (int j = 0; j < gridSize * 3; j++) {
                if (expandGrid[i][j] == 0) {
                    floodfill(expandGrid, i, j);
                    regionCount++;
                }
            }
        }
        
        return regionCount;
    }

    private void floodfill(int[][] expandedGrid, int row, int col) {
        Queue<int[]> q = new LinkedList<>();
        expandedGrid[row][col] = 1;
        q.add(new int[]{row, col});
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            for (int[] direction : DIRECTIONS) {
                int newRow = direction[0] + cell[0];
                int newCol = direction[1] + cell[1];
                if (isValidCell(expandedGrid, newRow, newCol)) {
                    expandedGrid[newRow][newCol] = 1;
                    q.add(new int[]{newRow, newCol});
                }
            }
        }
    }

    private boolean isValidCell(int[][] expandedGrid, int row, int col) {
        int n = expandedGrid.length;
        return (row >= 0 && col >= 0 && row < n && col < n && expandedGrid[row][col] == 0);
    }
}

