# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # TODO: Write your code here
  if head is None or head.next is None:
    return True

  fast = head
  slow = head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next

  head_second_half = reverse(slow)
  copy_head_second_half = head_second_half

  while (head is not None and head_second_half is not None):
    if head.value != head_second_half.value:
      break
    head = head.next
    head_second_half = head_second_half.next
  
  reverse(copy_head_second_half)

  if head is None or head_second_half is None:
    return True
  
  return False


def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
