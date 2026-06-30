# Problem:
# Sort Colors
#
# Approach:
# Use the Dutch National Flag Algorithm.
# Maintain three pointers:
# - low: next position where 0 should be placed.
# - mid: current element being examined.
# - high: next position where 2 should be placed.
#
# While scanning with the mid pointer:
# - If the current element is 0, swap it with low and move both pointers.
# - If it is 1, simply move mid.
# - If it is 2, swap it with high and move high only, since the new element at mid
#   has not been examined yet.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1