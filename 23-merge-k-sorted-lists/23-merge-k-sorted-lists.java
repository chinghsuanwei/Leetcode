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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>((a, b) -> (a.val - b.val));
        
        for(ListNode node : lists)
        {
            if(node != null)
            {
                pq.offer(node);
            }
        }
        
        ListNode sentinel = new ListNode(0);
        ListNode curr = sentinel;
        while(pq.size() > 0)
        {
            ListNode node = pq.poll();
            curr.next = node;
            
            curr = node;
            
            if(node.next != null) pq.offer(node.next);
        }
        
        return sentinel.next;
    }
}