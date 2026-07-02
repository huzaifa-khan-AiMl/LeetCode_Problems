# Problem:
# Missing Number
#
# Approach:
# Compute the expected sum of numbers from 0 to n using the arithmetic
# series formula. Then subtract the actual sum of the array. The difference
# is the missing number.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        return total - sum(nums)