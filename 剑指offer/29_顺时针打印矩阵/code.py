from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        s_length, e_length, s_width, e_width, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []

        while True:
            for j in range(s_length, e_length + 1):
                res.append(matrix[s_width][j])
            s_width += 1
            if s_width > e_width:
                break

            for j in range(s_width, e_width + 1):
                res.append(matrix[j][e_length])
            e_length -= 1
            if s_length > e_length:
                break

            for j in range(e_length, s_length - 1, -1):
                res.append(matrix[e_width][j])
            e_width -= 1
            if s_width > e_width:
                break

            for j in range(e_width, s_width - 1, -1):
                res.append(matrix[j][s_length])
            s_length += 1
            if s_length > e_length:
                break
        return res


if __name__ == '__main__':
    print(list(range(10, 0)))
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
