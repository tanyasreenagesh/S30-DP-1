# Time Complexity : O(n) where n is the number of houses
# Space Complexity : O(n) for memoized array
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

'''
Keep a memoized index of max possible loot at any house index.
Recursively either choose or don't choose that house to rob.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.helper(nums, 0, memo)

    def helper(self, nums: List[int], idx: int, memo: Dict[int, int]):
        if idx >= len(nums):
            return 0

        # already computed this index max loot
        if idx in memo:
            return memo[idx]
        
        # choose
        choose = nums[idx] + self.helper(nums, idx+2, memo)

        # not choose
        notChoose = self.helper(nums, idx+1, memo)

        memo[idx] = max(choose, notChoose)
        return memo[idx]