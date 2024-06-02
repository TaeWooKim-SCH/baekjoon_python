N, B = map(int, input().split());

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
answer = '';

while N:
  answer += alphabet[N % B];
  N //= B;

print(answer[::-1]);

