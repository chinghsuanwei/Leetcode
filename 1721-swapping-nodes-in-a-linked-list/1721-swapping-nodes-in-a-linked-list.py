# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getSizehOfLinkedList(self, head: Optional[ListNode]) -> int:
        
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        return count
    
    def findPreviousNode(self, head: Optional[ListNode], sentinel: Optional[ListNode], k:int) -> Optional[ListNode]:
        
        count = 1
        
        pre = sentinel
        while head:
            if count == k :
                return pre
            
            count += 1
            
            pre = head
            head = head.next
        
        return pre
    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #find length and also kth node
        
        #sentinel = ListNode()
        #sentinel.next = head
        
        
        
        n = self.getSizehOfLinkedList(head)
        
        if k == n - k + 1:
            return head
        
        sentinel = ListNode()
        sentinel.next = head
        
        pre1 = self.findPreviousNode(head, sentinel, k)
        pre2 = self.findPreviousNode(head, sentinel, n - k + 1)
          
        # P1  N1 N2
        # O  O　O
        if pre1.next == pre2:
            
            #print("Test 1")
            
            #node2 insert to pre1 next    
            node1 = pre1.next
            node2 = pre2.next
            
            next1 = node1.next
            next2 = node2.next
            
            pre1.next = node2
            
            node1.next = next2
            node2.next = node1
            
            
        elif pre2.next == pre1:
            #node1 insert to pre2 next
            
            #print("Test 2")
            
            # P2  N2 N1
            # O  O　O
            
            node1 = pre1.next
            node2 = pre2.next
            
            next1 = node1.next
            next2 = node2.next
            
            pre2.next = node1
            
            node2.next = next1
            node1.next = node2
            
        else:
            
            # P1 N1  P2 N2
            # O  O O O　O
            
            
            
            node1 = pre1.next
            node2 = pre2.next
            
            #print(node1.val)
            
            next1 = node1.next
            next2 = node2.next
            
            pre1.next = node2
            pre2.next = node1
            
            node1.next = next2
            node2.next = next1
            
        
        
        return sentinel.next