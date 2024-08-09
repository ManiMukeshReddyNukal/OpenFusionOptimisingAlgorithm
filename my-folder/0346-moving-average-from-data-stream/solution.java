class MovingAverage {
    Deque<Integer> dq;
    int cap;
    int sum;

    public MovingAverage(int size) {
        dq=new LinkedList<Integer>();
        cap=size;
        sum=0;
    }
    
    public double next(int val) {
        sum+=val;
        if(dq.size()==cap){
            sum-=dq.removeLast();
        }
        dq.addFirst(val);
        return sum/(double)dq.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
