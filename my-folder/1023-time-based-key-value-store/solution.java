class TimeMap {
    HashMap<String,TreeMap<Integer,String>> cache;

    public TimeMap() {
        cache=new HashMap<String,TreeMap<Integer,String>>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!cache.containsKey(key)){
            cache.put(key,new TreeMap<Integer,String>());
        }
        cache.get(key).put(timestamp,value);
    }
    
    public String get(String key, int timestamp) {
        if(!cache.containsKey(key)){
            return "";
        }
        Integer floorkey= cache.get(key).floorKey(timestamp);
        if(floorkey!=null){
            return cache.get(key).get(floorkey);
        }
        return "";
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
