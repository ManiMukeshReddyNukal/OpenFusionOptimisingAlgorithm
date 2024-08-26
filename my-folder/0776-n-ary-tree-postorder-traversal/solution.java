/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {

        List<Integer> resp = new ArrayList<>();
        helper(resp, root);
        return resp;
        
    }
    private void helper(List<Integer> resp, Node node){
        if (node==null){
            return;
        }
        for( Node child : node.children){
            helper(resp,child);
        }
        resp.add(node.val);
    }
}
