class MinStack {
    Deque<int[]> deque;

    public MinStack() {
        deque=new LinkedList<>();
    }
    
    public void push(int val) {
        if (deque.isEmpty()){
            deque.addLast(new int[]{val,val});
        }
        else{
            int mini=Math.min(val,deque.peekLast()[1]);
        deque.addLast(new int[]{val,mini});
        }
        
    }
    
    public void pop() {
        deque.pollLast();
    }
    
    public int top() {
        return deque.peekLast()[0];
    }
    
    public int getMin() {
        return deque.peekLast()[1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
