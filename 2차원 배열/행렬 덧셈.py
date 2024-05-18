N, M = list(map(int, input().split(' ')));

A = [];
B = [];

for _ in range(N):
  row = list(map(int, input().split(' ')));
  A.append(row);
for _ in range(N):
  row = list(map(int, input().split(' ')));
  B.append(row);

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

