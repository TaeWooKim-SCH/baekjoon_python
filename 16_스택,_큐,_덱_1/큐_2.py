import sys;

class CircularQueue:
    def __init__(self, MAX_QSIZE):
        self.MAX_QSIZE = MAX_QSIZE;
        self.front = 0;
        self.rear = 0;
        self.items = [None] * self.MAX_QSIZE;
    def __len__(self):
        return (self.rear - self.front + self.MAX_QSIZE) % self.MAX_QSIZE;
    def isEmpty(self):
        return self.front == self.rear;
    def isFull(self):
        return self.front == (self.rear + 1) % self.MAX_QSIZE;
    def enqueue(self, item):
        if (not self.isFull()):
            self.rear = (self.rear + 1) % self.MAX_QSIZE;
            self.items[self.rear] = item;
    def dequeue(self):
        if (not self.isEmpty()):
            self.front = (self.front + 1) % self.MAX_QSIZE;
            return self.items[self.front];

N = int(sys.stdin.readline());
queue = CircularQueue(2_000_000);

for _ in range(N):
    cmd_list = list(sys.stdin.readline().rstrip('\n').split(' '));
    cmd = cmd_list[0];
    if (cmd == "push"):
        queue.enqueue(int(cmd_list[1]));
    elif (cmd == "pop"):
        if (queue.isEmpty()):
            print(-1);
        else:
            print(queue.dequeue());
    elif (cmd == "size"):
        print(queue.__len__());
    elif (cmd == "empty"):
        if (queue.isEmpty()):
            print(1);
        else:
            print(0);
    elif (cmd == "front"):
        if (queue.isEmpty()):
            print(-1);
        else:
            print(queue.items[queue.front + 1]);
    elif (cmd == "back"):
        if (queue.isEmpty()):
            print(-1);
        else:
            print(queue.items[queue.rear]);