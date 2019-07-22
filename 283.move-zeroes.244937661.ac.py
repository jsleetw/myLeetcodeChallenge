class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        
        nums_len = len(nums)
        count_time = 1
        index = 0
        while count_time <= nums_len:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
                #print(nums)
                if index <= 0:
                    index = 0
                    count_time +=1
                else:
                    index -= 1
            else:
                index +=1
                count_time +=1
        
        
