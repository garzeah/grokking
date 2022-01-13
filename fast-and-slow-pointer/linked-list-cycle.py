class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True

        except:
            return False

# Time Complexity: Therefore, the time complexity of our algorithm
# will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

# Space Complexity: O(1)
