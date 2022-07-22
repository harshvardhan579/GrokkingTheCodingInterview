# Check if a number is Happy Number or not

def find_happy_number(num):
  # TODO: Write your code here
  fast = num
  slow = num
  while True:
    slow = find_square_sum(slow)
    fast = find_square_sum(find_square_sum(fast))
    if fast == slow:
      break
  return slow == 1

def find_square_sum(num):
  sm = 0
  while (num > 0):
    digit = num%10
    sm += digit*digit
    num //= 10
  return sm


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
