__author__ = 'Darr_en1'

"""
    设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

    循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

    你的实现应该支持如下操作：

    MyCircularQueue(k): 构造器，设置队列长度为 k 。
    Front: 从队首获取元素。如果队列为空，返回 -1 。
    Rear: 获取队尾元素。如果队列为空，返回 -1 。
    enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
    deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
    isEmpty(): 检查循环队列是否为空。
    isFull(): 检查循环队列是否已满。
"""
class MyCircularQueue:
    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k+1
        self.queue = [None] * self.k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            print("is full")
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear+1) % self.k
            return True

    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            print("is empty")
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.k
            return True


    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        return (self.rear+1 - self.front)%self.k == 0


if __name__ == '__main__':
    q = MyCircularQueue(3)
    print(q.queue,q.Rear(),q.Front())
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(4))
    print(q.enQueue(5))
    print(q.deQueue())

    print(q.queue,q.Rear(),q.Front())
