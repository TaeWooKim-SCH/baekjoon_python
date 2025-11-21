T = int(input());

for _ in range(T):
    parenthesis_string = input();
    stack = [];
    stack_size = 0;
    out_of_range = False;
    
    for parenthesis in parenthesis_string:
        if (parenthesis == "("):
            stack.append(parenthesis);
            stack_size += 1;
        else:
            if (stack_size == 0):
                out_of_range = True;
                break;
            else:
                stack.pop();
                stack_size -= 1;
    if ((stack_size == 0) and (not out_of_range)):
        print("YES");
    else:
        print("NO");