import sys;

N = int(input());
stack = [];
stack_size = 0;

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split(" ")));

    if (command[0] == 1):
        stack.append(command[1]);
        stack_size += 1;
    
    if (command[0] == 2):
        if (stack_size != 0):
            print(stack.pop());
            stack_size -= 1;
        else:
            print(-1);
    
    if (command[0] == 3):
        print(stack_size);
    
    if (command[0] == 4):
        if (stack_size != 0):
            print(0);
        else:
            print(1);
    
    if (command[0] == 5):
        if (stack_size != 0):
            print(stack[stack_size - 1]);
        else:
            print(-1);