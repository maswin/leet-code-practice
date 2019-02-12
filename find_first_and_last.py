# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def __init__(self):
        self.first = -1
        self.last = -1

    def find_position(self, nums, target, start, end, ff, fl):
        if start > end or (not ff and not fl):
            return
        mid = int((start + end) / 2)
        if nums[mid] == target:
            if (mid == start or nums[mid - 1] != target) and ff:
                self.first = mid
            else:
                self.find_position(nums, target, start, mid - 1, ff, False)
            if (mid == end or nums[mid + 1] != target) and fl:
                self.last = mid
            else:
                self.find_position(nums, target, mid + 1, end, False, fl)
        elif nums[mid] < target:
            self.find_position(nums, target, mid + 1, end, ff, fl)
        else:
            self.find_position(nums, target, start, mid - 1, ff, fl)

    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        self.find_position(nums, target, 0, len(nums) - 1, True, True)
        return [self.first, self.last]


if __name__ == "__main__":
    assert Solution().searchRange([1, 2, 3], 2) == [1, 1]
    assert Solution().searchRange([1, 2, 2, 3], 2) == [1, 2]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([3, 3, 3], 3) == [0, 2]
