### 원래 줄이 비어있을 때, 빈 공간 줄이 비어있을 때, 둘 다 차있을 때로 분기처리
import sys

N = int(sys.stdin.readline()); # 1 <= N <= 1,000 자연수
num_list = list(map(int, sys.stdin.readline().split(" ")));

stack = [];
target = 1;

while (True):
    if (target == N):
        print("Nice");
        break; 

    is_empty_stack = len(stack) == 0;
    is_empty_num_list = len(num_list) == 0;
        
    if (is_empty_stack and (not is_empty_num_list)):
        num_list_first = num_list.pop(0);
        if (num_list_first == target):
            target += 1;
        else:
            stack.append(num_list_first);
    elif ((not is_empty_stack) and is_empty_num_list):
        if (stack.pop() == target):
            target += 1;
        else:
            print('Sad');
            break;
    else:
        if (num_list[0] == target):
            num_list.pop(0);
            target += 1;
        elif (stack[-1] == target):
            stack.pop();
            target += 1;
        else:
            if (num_list[0] < stack[-1]):
                stack.append(num_list.pop(0));
            else:
                print('Sad');
                break;