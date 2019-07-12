class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Approach 1
        #time: O(n^2)
        #space: O(1)
        #method 1
        #2 for loop in for loop 
        #for i in range(0, len(nums) -1):
        #    first_num = nums[i] # 2
        #    for j in range(i+1, len(nums)): # 7
        #        sec_num = nums[j]
        #        if first_num + sec_num == target:
        #            return [i, j]
        #method 2
        #use arr
        tmp_arr = {}
        for k, v in enumerate(nums):
            match_num = target - v
            if match_num in tmp_arr:
                return [tmp_arr[match_num], k]
            else:
                tmp_arr[v] = k
        return
