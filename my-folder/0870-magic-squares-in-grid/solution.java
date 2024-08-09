class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int resp=0;
        for (int row=0; row+2<grid.length; row++){
            for (int col=0; col+2<grid[0].length; col ++){
                if(isMagicSq(grid,row,col)){
                    resp+=1;
                }
            }
        }
        return resp;
    }
    public boolean isMagicSq(int[][] grid, int row, int col){
        String seq="2943816729438167";
        String reverseseq="7618349276183492";
        StringBuilder sb = new StringBuilder();
        int[] borders=new int[] {0,1,2,5,8,7,6,3};
        for (int i: borders){
            sb.append(grid[row+(i/3)][col+(i%3)]);
        }
        String border=sb.toString();
        return ( (grid[row][col]%2==0) && (seq.contains(border)||reverseseq.contains(border)) && grid[row+1][col+1]==5);
    }
}
