def reversebasket(n, m):
  basket = [i for i in range(1, n + 1)];
  for _ in range(m):
    i, j = list(map(int, input().split(' ')));
    basket[i - 1:j] = reversed(basket[i - 1:j]);
  return ' '.join(map(str, basket));

n, m = list(map(int, input().split(' ')));
print(reversebasket(n, m));