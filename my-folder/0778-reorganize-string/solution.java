class Solution {
    public String reorganizeString(String s) {
        int n=1;
        HashMap<Character, Integer> map=new HashMap<>();
        for(int i = 0; i < s.length(); i++) 
        {
            char x = s.charAt(i);
            map.put(x, map.getOrDefault(x, 0)+1);
        }
        PriorityQueue<Map.Entry<Character, Integer>> pq =new PriorityQueue<Map.Entry<Character, Integer>>((e1, e2) -> e2.getValue()-e1.getValue());
        pq.addAll(map.entrySet());
        PriorityQueue<Map.Entry<Character, Integer>> q =new PriorityQueue<Map.Entry<Character, Integer>>((e1, e2) -> e2.getValue()-e1.getValue());
        String res="";
        while(!pq.isEmpty()){
            for(int i=0; i<=n; i++){
                if(!pq.isEmpty()){
                    Map.Entry<Character, Integer> entry = pq.poll();
                    entry.setValue(entry.getValue() - 1);
                    if(entry.getValue()!=0){
                        q.add(entry);
                    }
                    res+=entry.getKey();
                    System.out.println(res);
                }else if(!q.isEmpty()){
                    System.out.println("Not possible");
                    return "";
                }else{
                    break;
                }
            }
            while(!q.isEmpty()){
                Map.Entry<Character, Integer> entry = q.poll();
                pq.add(entry);
            }
        }
        return res;
    }
}
