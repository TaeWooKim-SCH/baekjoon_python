import sys

N = int(sys.stdin.readline()); # 1 <= N <= 1,000 자연수
num_list = list(map(int, sys.stdin.readline().split(" ")));

stack = [];
stack_size = 0;
target = 1;

while (True):
    if (target == N):
        print("Nice");
        break; 

    is_empty_stack = stack_size == 0;
    is_empty_num_list = len(num_list) == 0;
        
    if (is_empty_num_list and (num_list[0] != target)):
        if (is_empty_stack and (stack[-1] == target)):
            stack.pop();
            target += 1;
        if (is_empty_stack and (stack[-1] < num_list[0])):
            print("Sad");
            break;
        stack.append(num_list.pop(0));
        stack_size += 1;
    elif (num_list == target):
        target += 1;
        num_list.pop(0);

### 원래 줄이 비어있을 때, 빈 공간 줄이 비어있을 때, 둘 다 차있을 때로 분기처리