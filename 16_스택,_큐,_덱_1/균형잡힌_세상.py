import sys

class Stack:
    def __init__(self):
        self.stack = [];
        self.stack_size = 0;
    def push(self, value):
        self.stack.append(value);
        self.stack_size += 1;
    def pop(self):
        el = self.stack.pop();
        self.stack_size -= 1;
        return el;

while (True):
    input = sys.stdin.readline().strip('\n');
    stack = Stack();
    valid = True;

    if (input == "."):
        break;

    for char in input:
        if (char == "(" or char == "["):
            stack.push(char);
        elif (char == ")"):
            if ((stack.stack_size == 0) or (stack.pop() != "(")):
                valid = False;
                break;
        elif (char == "]"):
            if ((stack.stack_size == 0) or (stack.pop() != "[")):
                valid = False;
                break;
    if (stack.stack_size == 0 and valid):
        print('yes');
    else:
        print('no');