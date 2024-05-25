N, B = list(input().split(' '));

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
answer = 0

for i in range(len(N)):
  answer += alphabet.index(N[i]) * (int(B) ** (len(N) - i - 1));

print(answer);