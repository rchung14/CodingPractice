# ARRAYS
class Solution(object):
    def findClosestNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closestNum = nums[0]
        for number in nums: 
            if abs(closestNum) > abs(number): 
                closestNum = number
            if abs(closestNum) == abs(number): 
                if closestNum < number:
                    closestNum = number
        
        return closestNum
    
    nums = [-1,2,3,4,1,100]
    print(findClosestNumber(nums))