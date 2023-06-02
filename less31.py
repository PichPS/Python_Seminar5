# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
   if n == 0 or n == 1:
      return 1
   return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))

# fib(4) - fib(3) + fib(2) = 2 + 1 + 1 + 1 = 5
#            |         |
#  fib(2) +    fib(1)    fib(1) + fib(0)
#    |             |         |       |
#fib(1) + fib(0)   1         1       1
#  1 +    1