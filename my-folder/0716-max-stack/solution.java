class MaxStack {

    TreeSet<int[]> stack;
    TreeSet<int[]> positions;
    int position;

    Comparator<int[]> comparator = (a,b)-> (a[0]==b[0])? a[1]-b[1]:a[0]-b[0];

    public MaxStack() {
        stack = new TreeSet<>(comparator);
        positions = new TreeSet<>(comparator);
        position=0;
        
    }
    
    public void push(int x) {
        stack.add(new int[]{position,x});
        positions.add(new int[]{x,position});
        position+=1;
    }
    
    public int pop() {
        int[] out = stack.pollLast();
        positions.remove(new int[] {out[1],out[0]});
        return out[1];
    }
    
    public int top() {
        return stack.last()[1];
    }
    
    public int peekMax() {
        return positions.last()[0];
    }
    
    public int popMax() {
        int[] out = positions.pollLast();
        stack.remove(new int[]{out[1],out[0]});
        return out[0];
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
