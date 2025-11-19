N = int(input());

x_locs = [];
y_locs = [];

for _ in range(N):
  x, y = map(int, input().split(' '));
  x_locs.append(x);
  y_locs.append(y);

x_locs.sort();
y_locs.sort();

print((max(x_locs) - min(x_locs)) * (max(y_locs) - min(y_locs)));