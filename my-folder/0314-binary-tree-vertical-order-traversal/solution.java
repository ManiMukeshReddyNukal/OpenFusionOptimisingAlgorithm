/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> resp = new ArrayList<>();
        if(root==null){
            return resp;
        }
        Map<Integer,ArrayList> mp = new TreeMap();
        Queue<Pair<TreeNode,Integer>> q = new ArrayDeque<>();
        int col = 0;
        q.offer(new Pair(root,0));
        while(!q.isEmpty()){
            Pair<TreeNode,Integer> pair = q.poll();
            TreeNode node = pair.getKey();
            if (node != null){
            int colo = pair.getValue();
            mp.putIfAbsent(colo, new ArrayList<>());
            mp.get(colo).add(node.val);
            q.offer(new Pair(node.left,colo-1));
            q.offer(new Pair(node.right,colo+1));
            }
            
        }
        return new ArrayList(mp.values());

    }
}
