import sys

K = int(sys.stdin.readline()); # 1 <= K <= 100,000
stack = [];
stack_acc = 0;

for _ in range(K):
    num = int(sys.stdin.readline()); # 0 <= num <= 1,000,000
    if (num == 0):
        stack_acc -= stack.pop();
    else:
        stack.append(num);
        stack_acc += num;

print(stack_acc);