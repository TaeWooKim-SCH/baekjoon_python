N, K = map(int, input().split(' '));

measure = [1];

for i in range(2, N + 1):
  if (N % i == 0):
    measure.append(i);
  if (len(measure) == K):
    print(measure[-1]);
    break;

if (len(measure) < K):
  print(0);