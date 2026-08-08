class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num=nums1+nums2
        num.sort()
        med=len(num)
        if(med%2==0):
            b=(num[(med//2)-1]+num[(med//2)])
            c=b/2.0
            return float(c)
        elif(med%2==1):
            j=num[med//2]
            return float(j)