class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = current_sum = nums[0]
        #print(current_sum)

        for num in nums[1:]:
            #print num
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            #print(current_sum, max_sum)
            #print("next")

        return max_sum
