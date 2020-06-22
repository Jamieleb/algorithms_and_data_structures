# Uses python3
import sys

def gcd_naive(a, b):
  current_gcd = 1
  for d in range(2, min(a, b) + 1):
    if a % d == 0 and b % d == 0:
      if d > current_gcd:
        current_gcd = d

  return current_gcd

def greatest_common_divisor(a, b):
  remainder = a % b
  if remainder == 0:
    return b
  else:
    return greatest_common_divisor(b, remainder)


if __name__ == "__main__":
  input = sys.stdin.readline()
  a, b = map(int, input.split())
  print(greatest_common_divisor(a, b))

