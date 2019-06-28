class Solution:
    """
    https://leetcode.com/problems/squares-of-a-sorted-array/discuss/310865/Python%3A-A-comparison-of-lots-of-approaches!-Sorting-two-pointers-deque-iterator-generator
    """
    @staticmethod
    def sortedSquares(_list: list) -> list:
        print(sorted([x * x for x in _list]))
        print(sorted(map(lambda x: pow(x, 2), _list)))


if __name__ == '__main__':
    Solution.sortedSquares([-7, -3, 2, 3, 11])
