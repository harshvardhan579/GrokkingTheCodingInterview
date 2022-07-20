# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  # TODO: Write your code here
  fast = head
  slow = head
  temp = []
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      cycle_length = calculateCycleLength(slow)
      break
  return find_start(head, cycle_length)

def calculateCycleLength(slow):
  current = slow
  cycleLen = 0
  while True:
    current = current.next
    cycleLen += 1
    if current == slow:
      break
  return cycleLen

def find_start(head, cycle_length):
  p1 = head
  p2 = head
  while cycle_length > 0:
    p2 = p2.next
    cycle_length -= 1
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next
  return p1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
