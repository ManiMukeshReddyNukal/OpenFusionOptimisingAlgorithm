/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodeset=new HashSet<>();
        ListNode current = head;
        while (current != null){
            if (nodeset.contains(current)){
                return true;
            }
            nodeset.add(current);
            current=current.next;
        }
        return false;
    }
}
