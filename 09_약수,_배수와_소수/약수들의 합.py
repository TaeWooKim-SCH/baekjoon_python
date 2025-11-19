while True:
  n = int(input());
  perfect_num = 1;
  answer = '{0} = 1'.format(n);

  if (n == -1):
    break;

  for i in range(2, (n // 2 + 1)):
    if (n % i == 0):
      perfect_num += i;
      answer += ' + {0}'.format(i);
  
  if (perfect_num == n):
    print(answer);
  else:
    print('{0} is NOT perfect.'.format(n));