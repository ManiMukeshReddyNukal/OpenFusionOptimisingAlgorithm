class Solution {
    public int minOperations(String[] logs) {
        int depth=0;
        for ( String log : logs){
            if (log.equals("./"))
            {

            }
            else if(log.equals("../")){
                if (depth>0){
                    depth--;
                }
            }
            else{
               depth++; 
            }
        }
        return depth;
    }
}
