class Solution(object):
    def singleNumber(self,nums):
        count=0
        for i in range(len(nums)):
            count=count^nums[i]
        return count