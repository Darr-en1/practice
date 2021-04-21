from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        arr = deque()
        res = []
        for i in range(k):  # 初始化窗口, 最新添加的内容是保证是最小的
            while arr and nums[i] > arr[-1]:
                arr.pop()
            arr.append(nums[i])
        res.append(arr[0])
        for j in range(k, len(nums)):
            if nums[j - k] == arr[0]:  # 窗口移动如果移除了最大值需要删除
                arr.popleft()
            while arr and nums[j] > arr[-1]:
                arr.pop()
            arr.append(nums[j])
            res.append(arr[0])
        return res


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

from collections import OrderedDict