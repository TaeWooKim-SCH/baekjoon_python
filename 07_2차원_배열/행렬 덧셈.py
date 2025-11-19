N, M = list(map(int, input().split(' ')));

A = [list(map(int, input().split(' '))) for _ in range(N)];
B = [list(map(int, input().split(' '))) for _ in range(N)];

def addMatrix(A, B):
  result = [];
  for i in range(len(A)):
    result_row = [];
    for j in range(len(A[i])):
      result_row.append(A[i][j] + B[i][j]);
    result.append(result_row);
  return result;

answer = addMatrix(A, B);

for i in range(len(answer)):
  print(' '.join(map(str, answer[i])));

