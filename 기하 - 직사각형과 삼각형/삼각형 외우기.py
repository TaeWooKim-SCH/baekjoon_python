angles = [int(input()) for _ in range(3)];

if (sum(angles) == 180):
  if (len(set(angles)) == 1):
    print('Equilateral');
  elif (len(set(angles)) == 2):
    print('Isosceles');
  else:
    print('Scalene');
else:
  print('Error');

