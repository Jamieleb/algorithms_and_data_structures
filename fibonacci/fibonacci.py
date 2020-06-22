# Uses python3
def calc_fib(n):
  fib_array = []
  for index in range(n + 1):
    if index == 0 or index == 1:
      fib_array.append(index)
    else:
      fib_array.append(fib_array[index - 1] + fib_array[index - 2])

  return fib_array[n]

n = int(input())
print(calc_fib(n))
