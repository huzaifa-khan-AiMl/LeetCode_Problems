# Problem:
# Rotate Array
#
# Approach:
# Used the Reverse Technique.
# First reverse the entire array.
# Then reverse the first k elements.
# Finally reverse the remaining n-k elements.
# The reverse() helper function is called three times with different
# left and right pointer values to reverse the required portions of the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)