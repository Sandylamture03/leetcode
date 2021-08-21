class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
​
        # approach: do binary search twice for left and right boundaries
​
        if len(nums) == 0:
            return [-1, -1]
​
        result = []
​
        # do binary search first time to find left boundary
        left, right = 0, len(nums) - 1
​
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]
​
            if mid_num < target:
                left = mid
            else:
                right = mid
​
        # target not found
        if nums[left] != target and nums[right] != target:
            return [-1, -1]
​
        # left + 1 == right
        result.append(left if nums[left] == target else right)
​
        # do binary search second time to find right boundary
        left, right = 0, len(nums) - 1
​
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_num = nums[mid]
​
            if mid_num > target:
                right = mid
            else:
                left = mid
​
        # left + 1 == right
        result.append(right if nums[right] == target else left)
​
        return result
