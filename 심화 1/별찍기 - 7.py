# 최대 길이가 N * 2 - 1임
# 처음 N * 2 - 1길이의 배열을 생성
# 9 // 2 -> 4 처음 별을 찍을 인덱스
# 9 // 2 - 1 / 9 // 2 + 1 다음 별을 찍을 인덱스
# 별 뒤쪽은 공백이 없어야 함.

N = int(input());
maxLen = 2 * N - 1;
board = [[' '] * maxLen for _ in range(N)];
for i in range(N):
  print(' ' * (N - i - 1) + '*' * (2 * i + 1));  
for j in range(N - 1, 0, -1):
  print(' ' * (N - j) + '*' * (2 * j - 1));
