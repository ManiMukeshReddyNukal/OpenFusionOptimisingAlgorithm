class TicTacToe {
    private int[] rows;
    private int[] cols;
    int diag;
    int antidiag;

    public TicTacToe(int n) {
        rows=new int[n];
        cols=new int[n];
        diag=0;
        antidiag=0;
    }
    
    public int move(int row, int col, int player) {
        int n = rows.length;
        int curplayer= (player==1)? 1:-1;
        rows[row]+=curplayer;
        cols[col]+=curplayer;
        if (row==col ){
            diag+=curplayer;
        }
        if(row+col==n-1){
            antidiag+=curplayer;
        }
        return ( Math.abs(rows[row])==n || Math.abs(cols[col])==n || Math.abs(diag)==n || Math.abs(antidiag)==n)? player:0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
