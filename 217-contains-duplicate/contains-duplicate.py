class Solution:
    def containsDuplicate(self, nums):

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return True

        #     seen.add(num)

        # return False
        if len(nums) == len(set(nums)):
            return False
        return True