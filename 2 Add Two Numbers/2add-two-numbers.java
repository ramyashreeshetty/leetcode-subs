import java.lang.Math;
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1==null) return l2;
        if(l2==null) return l1;
        
        int carry=0;
        ListNode newnode=new ListNode(0);
        ListNode temp=newnode;
        
        while(l1!=null || l2!=null){
            int v1=(l1==null) ? 0 : l1.val;
            int v2=(l2==null) ? 0 : l2.val;
            
            int sum=v1+v2+carry;
            temp.next=new ListNode(sum%10);
            carry=sum/10;
            
            temp=temp.next;
            if(l1!=null) l1=l1.next;
            if(l2!=null) l2=l2.next;
        }
        
        if(carry!=0){
            temp.next=new ListNode(carry);
        }
        return newnode.next;
        
        
    }
}