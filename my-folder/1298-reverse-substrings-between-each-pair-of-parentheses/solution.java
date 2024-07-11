class Solution {
    public String reverseParentheses(String s) {
        Stack<Integer> openbracket= new Stack<>();
        StringBuilder str=new StringBuilder();
        for ( char ch : s.toCharArray()){
            if (ch=='('){
                openbracket.push(str.length());
            }
            else if ( ch == ')'){
                int start = openbracket.pop();
                reverse(str, start, str.length()-1);
            }
            else{
                str.append(ch);
            }
        }
        return str.toString();
    }

    public void reverse(StringBuilder sb, int start, int end){
        while (start<end){
            char temp=sb.charAt(start);
            sb.setCharAt(start++, sb.charAt(end));
            sb.setCharAt(end--, temp);
        }
    }
}
