class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_list, self.stack = [], []

    def push(self, x: int) -> None:
        # >= 保证多个最小值都存储
        if not self.min_list or self.min_list[-1] >= x:
            self.min_list.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
            if x == self.min_list[-1]:
                self.min_list.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def min(self) -> int:
        if self.min_list:
            return self.min_list[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.min()
