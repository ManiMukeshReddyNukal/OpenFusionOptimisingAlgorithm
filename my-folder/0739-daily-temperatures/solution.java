class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] resp = new int[temperatures.length];
        Arrays.fill(resp,0);
        for (int i=0; i< temperatures.length; i++){
            while( !stack.isEmpty() && temperatures[i]> temperatures[stack.peek()] ){
                resp[stack.peek()]=i-stack.peek();
                stack.pop();
            }
            stack.push(i);
        }
        return resp;
    }
}
