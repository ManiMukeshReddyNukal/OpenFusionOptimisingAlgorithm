class Solution {
    private static final Map<String, BiFunction<Integer,Integer,Integer>> operations=new HashMap<>();

    static{
        operations.put("+", (a,b)-> a+b);
        operations.put("-", (a,b)-> a-b);
        operations.put("*", (a,b)-> a*b);
        operations.put("/", (a,b)-> a/b);
    }
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        for(String st : tokens){
            if (!operations.keySet().contains(st))
            {
                stack.push(Integer.valueOf(st));
                continue;
            }
            int number2=stack.pop();
            int number1=stack.pop();
            BiFunction<Integer,Integer,Integer> op=operations.get(st);
            int result = op.apply(number1, number2);
            stack.push(result);
        }
        return stack.pop();
    }
}
