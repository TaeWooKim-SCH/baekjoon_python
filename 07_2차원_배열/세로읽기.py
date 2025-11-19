words = [];

for _ in range(5):
  word = input();
  for j in range(len(word)):
    if (len(words) <= j):
      words.append(word[j]);
    else:
      words[j] += word[j];

print(''.join(words));