class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        List<List<Integer>> output = new ArrayList<>();
        int[][] dir = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int totalCells = rows * cols;
        int steps = 0;
        int d = 0; // direction index

        output.add(Arrays.asList(rStart, cStart));

        while (output.size() < totalCells) {
            if (d == 0 || d == 2) {
                steps++;
            }
            for (int i = 0; i < steps; i++) {
                rStart += dir[d][0];
                cStart += dir[d][1];

                if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) {
                    output.add(Arrays.asList(rStart, cStart));
                }
            }
            d = (d + 1) % 4; // move to the next direction
        }

        return output.stream().map(innerList -> innerList.stream().mapToInt(Integer::intValue).toArray()).toArray(int[][]::new);
    }
}

