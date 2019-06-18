class Person:
    """
    __eq__(self, other) 定义了等号的行为, == 。

    __ne__(self, other) 定义了不等号的行为, != 。

    __lt__(self, other) 定义了小于号的行为， < 。

    __gt__(self, other) 定义了大于等于号的行为， >= 。
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # 消除两边的尖括号
        return f"Person {self.name}:{self.age}"

    def __eq__(self, other):
        return (self.age, self.name) == (other.age, other.name)

    def __lt__(self, other):
        return (self.age, self.name) < (other.age, other.name)


if __name__ == '__main__':
    p1 = Person('A', 100)
    p2 = Person('B', 95)
    p3 = Person('C', 95)

    print(p1 > p2)
    print(p2 > p3)
