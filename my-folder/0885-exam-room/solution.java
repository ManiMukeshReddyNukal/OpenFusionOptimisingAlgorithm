class ExamRoom {
    TreeSet<Integer> set;
    int space;
    public ExamRoom(int n) {
        set = new TreeSet<>();
        space=n-1;
    }
    
    public int seat() {
        if(set.size()==0){
            set.add(0);
            return 0;
        }
        int left=set.first();
        int diff = left-0;
        int max=0;
        for (Integer right : set){
            if (right==left) continue;
            int mid=left+(right-left)/2;
            if (diff < Math.min(mid-left,right-mid) && !set.contains(mid)){
                diff=Math.min(mid-left,right-mid);
                max=mid;
            }
            left=right;
        }
        int last = set.last();
        if (space-last > diff) max=space;
        set.add(max);
        return max;

    }
    
    public void leave(int p) {
        set.remove(p);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
