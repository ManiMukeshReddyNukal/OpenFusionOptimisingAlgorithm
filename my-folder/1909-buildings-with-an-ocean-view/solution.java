class Solution {
    public int[] findBuildings(int[] heights) {
        Deque<Integer> deque = new LinkedList<>();
        for(int i=0; i< heights.length; i++){
            while ( ! deque.isEmpty() && heights[i] >= heights[deque.peekLast()])
            {
                deque.pollLast();
            }
            deque.addLast(i);
        }
        return deque.stream().mapToInt(Integer::intValue).toArray();
    }
}
