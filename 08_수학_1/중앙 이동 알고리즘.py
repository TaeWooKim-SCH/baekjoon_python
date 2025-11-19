N = int(input());

result = 2;

for _ in range(0, N):
  result = 2 * result - 1;

print(result ** 2);