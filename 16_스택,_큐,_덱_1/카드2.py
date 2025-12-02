# 1부터 N까지 카드
# 1번 카드가 제일 위, N번 카드가 제일 아래
# 제일 위 -> 바닥에 버림
# 제일 위에 있는 카드 -> 제일 아래로 옮김
# 1234 -> 1버림 -> 234 -> 맨 위 카드 제일 아래로 -> 342
# 3버림 -> 42 -> 제일 아래로 -> 24
# 2버림

import sys;

class CircularQueue:
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.items = [None] * self.MAX_SIZE;
        self.front = 0;
        self.rear = 0;
    def isEmpty(self):
        return self.front == self.rear;
    def isFull(self):
        return self.front == (self.rear + 1) % self.MAX_SIZE;
    def length(self):
        return (self.rear - self.front + self.MAX_SIZE) % self.MAX_SIZE;
    def enqueue(self, item):
        if (not self.isFull()):
            self.rear = (self.rear + 1) % self.MAX_SIZE;
            self.items[self.rear] = item;
    def dequeue(self):
        if (not self.isEmpty()):
            self.front = (self.front + 1) % self.MAX_SIZE;
            return self.items[self.front];

N = int(sys.stdin.readline());
queue = CircularQueue(1_000_000);

for num in range(1, N + 1):
    queue.enqueue(num);

while (queue.length() > 1):
    if (queue.length() <= 1):
        break;
    queue.dequeue();
    num = queue.dequeue();
    queue.enqueue(num);

print(queue.items[queue.rear]);