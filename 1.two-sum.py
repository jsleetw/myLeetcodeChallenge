"""
[1] Two Sum

https://leetcode.com/problems/two-sum/description/

* algorithms
* Easy (44.30%)
* Total Accepted:    1.9M
* Total Submissions: 4.3M
* Testcase Example:  '[2,7,11,15]\n9'

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution():
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
        #t O(n)
        #s O(n)
        tmp_arr = {}
        for k, v in enumerate(nums):
            match_num = target - v
            if match_num in tmp_arr:
                return [tmp_arr[match_num], k]
            else:
                tmp_arr[v] = k
        return False
    
if __name__=="__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))