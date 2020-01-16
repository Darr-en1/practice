class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area, start, end = 0, 0, len(height) - 1
        while end > start:
            max_area = max(max_area, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
