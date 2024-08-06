class MedianFinder {

    PriorityQueue<Integer> minq;
    PriorityQueue<Integer> maxq;
    public MedianFinder() {
        minq = new PriorityQueue<>();
        maxq = new PriorityQueue<>(Collections.reverseOrder());
    }
    
    public void addNum(int num) {
        maxq.add(num);
        if( maxq.size()>0 && minq.size()>0 && maxq.peek()>minq.peek()){
            Integer val=maxq.poll();
            minq.add(val);
        }
        if (minq.size()>maxq.size()+1){
            Integer val=minq.poll();
            maxq.add(val);
        }
        if (maxq.size()>minq.size()+1){
            Integer val=maxq.poll();
            minq.add(val);
        }
        
    }
    
    public double findMedian() {
        if(minq.size()==maxq.size()){
            return (minq.peek()+maxq.peek())/2.0;
        }
        else if(minq.size()>maxq.size()){
            return minq.peek();
        }
        else{
            return maxq.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
