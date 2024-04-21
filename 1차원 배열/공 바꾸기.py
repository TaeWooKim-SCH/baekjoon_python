n, m = list(map(int, input().split(' ')));

def basketball(n, m):
  basket = [num for num in range(1, n + 1)];
  for num in range(m):
    i, j = list(map(int, input().split(' ')));
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]
  return ' '.join(map(str, basket));

print(basketball(n, m));