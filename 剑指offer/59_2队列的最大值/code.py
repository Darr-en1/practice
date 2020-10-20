from collections import deque


class MaxQueue:
    # 需要认识到元素只能冲左侧写入

    def __init__(self):
        self.a = deque()
        self.b = deque()

    def max_value(self) -> int:
        return self.b[0] if self.b else -1

    def push_back(self, value: int) -> None:
        while self.b and value > self.b[-1]:
            self.b.pop()
        self.b.append(value)
        self.a.append(value)

    def pop_front(self) -> int:
        if not self.a:
            return -1
        if self.a[0] == self.b[0]:
            self.b.popleft()
        return self.a.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
