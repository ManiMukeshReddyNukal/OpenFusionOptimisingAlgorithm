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
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> resp = new ArrayList();
        if(root==null) return resp;
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root);
        double sum = 0;
        
        while(!queue.isEmpty())
        {
            sum=0;
            int size = queue.size();
            for(int i=0;i<size;i++)
            {
                TreeNode currentNode=queue.poll();
                sum+=currentNode.val;
                if(currentNode.left!=null) queue.offer(currentNode.left);
                if(currentNode.right!=null) queue.offer(currentNode.right);
            }
            resp.add(sum/size);
        }

        return resp;
    }
}
