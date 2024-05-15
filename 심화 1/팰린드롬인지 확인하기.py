str = input();

def palindrome(string):
  compare = list(string);
  compare.reverse();
  compare = ''.join(compare);
  if (string == compare):
    return 1;
  else:
    return 0;

print(palindrome(str));