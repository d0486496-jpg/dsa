class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        if(nums==0):
            return 0
        elif(nums!=0):
            b=(len(nums))//2
            c=int(b)
            return nums[c]

        