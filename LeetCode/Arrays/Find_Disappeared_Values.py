# Problem:
# Find All Numbers Disappeared in an Array
#
# Approach:
# We use the In-Place Index Marking technique. Since every number is in the
# range [1, n], each value can be mapped to an index (value - 1). We mark
# the corresponding index as negative to indicate that the number has been
# seen. After marking, any index that still contains a positive value
# represents a missing number, so we add (index + 1) to the result.
#
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary space (excluding the output list)

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result