# Contains Duplicate
# Approach: set to track seen numbers
# Time: O(n) | Space: O(n)

class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False