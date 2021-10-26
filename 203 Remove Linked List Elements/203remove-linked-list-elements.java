/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode node = head;
        
        while (node != null) {
             if (node.next != null && node.next.val == val) {
                node.next = node.next.next;
            }else {

                node = node.next;
            }
        }
        
        //to check for the first node
        if(head!=null){
            if(head.val == val){
                return head.next;
            }
        }
        return head;
    }
}