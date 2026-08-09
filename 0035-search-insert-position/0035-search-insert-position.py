class Solution(object):
    def searchInsert(self, nums, target):
       first=0
       second=len(nums)-1
       while first<=second:
        mid=(first+second)//2
        if(nums[mid]>target):
            second=mid-1
        elif(nums[mid]==target):
            return mid
        else:
            first=mid+1
       return first
      

        