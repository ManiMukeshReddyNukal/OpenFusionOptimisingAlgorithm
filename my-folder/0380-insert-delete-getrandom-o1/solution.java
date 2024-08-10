class RandomizedSet {
    Map<Integer,Integer> map;
    List<Integer> lst;
    Random rand = new Random(); 

    public RandomizedSet() {
        map = new HashMap();
        lst=new ArrayList();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        map.put(val,lst.size());
        lst.add(lst.size(),val);
        return true;
    }
    
    public boolean remove(int val) {
        if(!map.containsKey(val)) return false;
        int idx=map.get(val);
        
        int temp = lst.get(lst.size()-1);
        // lst.set(lst.size()-1,val);
        lst.set(idx,temp);
        map.put(temp,idx);
        lst.remove(lst.size()-1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        return lst.get(rand.nextInt(lst.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
