N = int(input());

init_area = [[0] * 100 for _ in range(100)];
answer_area = 0;

for _ in range(N):
    x, y = list(map(int, input().split(' ')));
    for x_i in range(10):
        for y_i in range(10):
            init_area[x + x_i][y + y_i] = 1;

for row in init_area:
    answer_area += row.count(1);

print(answer_area);


