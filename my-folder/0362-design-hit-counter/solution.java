class HitCounter {
    int total;
    Deque<Pair<Integer,Integer>> hits;

    public HitCounter() {
        total=0;
        hits=new LinkedList<Pair<Integer,Integer>>();

    }
    
    public void hit(int timestamp) {
        if (hits.isEmpty() || hits.getLast().getKey()!=timestamp)
        {
            hits.add(new Pair<Integer,Integer>(timestamp,1));
        }
        else{
            int prevCount = hits.getLast().getValue();
            hits.removeLast();
            hits.add(new Pair<Integer,Integer>(timestamp,prevCount+1));
        }
        total++;
    }
    
    public int getHits(int timestamp) {
        while(!hits.isEmpty() && hits.getFirst().getKey() <= timestamp-300){
            total-=hits.getFirst().getValue();
            hits.removeFirst();
        }
        return total;
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
