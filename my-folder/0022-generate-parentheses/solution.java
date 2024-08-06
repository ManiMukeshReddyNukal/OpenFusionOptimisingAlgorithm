class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> output = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        backtracking(0, 0, sb, output, n);
        return output;
    }

    private void backtracking(int left, int right, StringBuilder sb, List<String> output, int n)
    {
        if (sb.length()==2*n){
            output.add(sb.toString());
            return;
        }
        if (left<n){
            sb.append("(");
            backtracking(left+1, right, sb, output, n);
            sb.deleteCharAt(sb.length()-1);
        }
        if (right<left){
            sb.append(")");
            backtracking(left,right+1,sb,output,n);
            sb.deleteCharAt(sb.length()-1);
        }

        }
    }
