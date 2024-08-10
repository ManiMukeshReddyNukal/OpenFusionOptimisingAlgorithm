class MedianFinder {

    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;

    public MedianFinder() {
        minHeap = new PriorityQueue();
        maxHeap = new PriorityQueue(Collections.reverseOrder());
    }
    
        public void addNum(int num) {
        // Add to maxHeap first
        maxHeap.add(num);
        
        // Balance by moving the largest in maxHeap to minHeap
        minHeap.add(maxHeap.poll());
        
        // Ensure minHeap never has more elements than maxHeap
        if (minHeap.size() > maxHeap.size()) {
            maxHeap.add(minHeap.poll());
        }
    }
    
    public double findMedian() {
        if(maxHeap.size()==minHeap.size()){
            return (minHeap.peek()+maxHeap.peek())/2.0;
        }
        return (maxHeap.size()>minHeap.size())? maxHeap.peek():minHeap.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
