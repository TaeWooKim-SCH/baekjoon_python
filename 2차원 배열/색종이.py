N = int(input());

init_area = 100 * N;

locations = [];
minus_area = 0;

for _ in range(N):
    x, y = list(map(int, input().split(' ')));
    locations.append((x, y));

locations.sort(key = lambda x: (x[0]));

for i in range(len(locations) - 1):
    x1, y1 = locations[i];
    x2, y2 = locations[i + 1];
    if (x1 - x2 < 10):
        minus_area += (10 - abs(x2 - x1)) * (10 - abs(y2 - y1));

print(init_area - minus_area);
