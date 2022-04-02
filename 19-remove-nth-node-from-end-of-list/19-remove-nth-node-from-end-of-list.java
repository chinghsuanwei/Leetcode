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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //if it's head
        //else
//         if(n==1){
//             head = head.next;
//         }
//         else {
//             ListNode cur = head;
//             ListNode pre = head;
//             for(int i=1; i<n; i++){
//                 pre = cur;
//                 cur = cur.next;
//             }
            
//             //node in the end
//             if(cur == null){
//                 pre.next = null; 
//             }
//             else{  //node in the middle
//                 pre.next = cur.next;   
//             }
            
//         }
        
        
        //find length
        ListNode cur = head;
        int length = 0;
        while(cur != null){
            cur = cur.next;
            length++;
        }
        
        n = length - n + 1;
        
        if(n==1){
            head = head.next;
        }
        else {
            cur = head;
            ListNode pre = head;
            for(int i=1; i<n; i++){
                pre = cur;
                cur = cur.next;
            }
            
            //node in the end
            if(cur == null){
                pre.next = null; 
            }
            else{  //node in the middle
                pre.next = cur.next;   
            }
            
        }
        
        return head;
    }
}