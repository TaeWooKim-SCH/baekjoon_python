max_num = 0;
answer_row = 1;
answer_col = 1;

for i in range(9):
  rows = list(map(int, input().split(' ')));
  rows_max = max(rows);
  if (max_num < rows_max):
    max_num = rows_max;
    answer_row = i + 1;
    answer_col = rows.index(max_num) + 1;

print(max_num);
print(answer_row, answer_col);