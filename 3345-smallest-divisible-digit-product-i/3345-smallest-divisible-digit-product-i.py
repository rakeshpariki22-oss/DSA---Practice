class Solution:

  def smallestNumber(self, n: int, t: int) -> int:
    def get_product(x):
      prod = 1
      while x > 0:
        prod *= x % 10
        x //= 10
      return prod

    for num in range(n, n + 10):
      if get_product(num) % t == 0:
        return num