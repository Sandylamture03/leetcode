/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
public ListNode removeElements(ListNode head, int val) {
ListNode newHead = removeElementsAux(head,head,val);
if (newHead!=null && head.val == val) return newHead.next;
return newHead;
}
​
private ListNode removeElementsAux(ListNode curr, ListNode prev, int val){
    if(curr == null )  return curr;
    removeElementsAux(curr.next,curr,val);
    if(curr.val == val){
        prev.next = curr.next;
    }
    return curr;   
}
}
