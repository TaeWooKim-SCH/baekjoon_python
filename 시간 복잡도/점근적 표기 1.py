# 모든 n0 < n <= 100에 대해 f(n) <= c x g(n)을 만족해야 함
# a1 = 7, a0 = 7
# c = 8
# n0 = 1
# f(n) = 7n + 7 g(1) = 8
a1, a0 = map(int, input().split(' '));
c = int(input());
n0 = int(input());

for num in range(n0, 101):
  if (a1 * num + a0 > c * num):
    print(0);
    break;
  if (num == 100):
    print(1);
