sticks = list(map(int, input().split(' ')));
max_stick = max(sticks);
remain_sticks = sticks.copy();
remain_sticks.remove(max_stick);

if (max_stick < sum(remain_sticks)):
  print(sum(sticks));
else:
  max_stick = sum(remain_sticks) - 1;
  print(max_stick + sum(remain_sticks));
