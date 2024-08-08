class Solution {

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> output = new ArrayList<>();
        char[][] current = new char[n][n];
        for(int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                current[i][j]='.';
            }
        }
        Set<Integer> diag = new HashSet<>();
        Set<Integer> antidiag = new HashSet<>();
        recursive(n, 0, current, output, diag, antidiag,new HashSet<>());
        return output;

    }

    public List<String> createBoard(char[][] current){
        List<String> resp = new ArrayList<>();
        for ( int row =0; row<current.length; row++){
            resp.add(new String(current[row]));
        }
        return resp;
    }


    public void recursive( int n,int i, char[][] current , List<List<String>> output, Set<Integer> diag, Set<Integer> antidiag, Set<Integer> colomns){
        if(i==n){
            output.add(createBoard(current));
            return;
        }
        for (int col=0; col<n;col++){
            int currentdiag=col-i;
            int currentantidiag=col+i;
            if ( !diag.contains(currentdiag) && !antidiag.contains(currentantidiag) && !colomns.contains(col)){
                current[i][col]='Q';
                diag.add(currentdiag);
                antidiag.add(currentantidiag);
                colomns.add(col);
                recursive(n,i+1,current,output,diag,antidiag,colomns);
                diag.remove(currentdiag);
                antidiag.remove(currentantidiag);
                colomns.remove(col);
                current[i][col]='.';
            }
        }

    }
}
