class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans_arr = []
        
        for x in xrange(len(nums) -2):
            if nums[x] == nums[x-1] and x > 0 :
                continue
            
            lp = x + 1
            rp = len(nums) - 1
        
            while lp < rp:
                sum = nums[x] + nums[lp] + nums[rp]
                if sum > 0:
                    rp -= 1
                elif sum < 0:
                    lp +=1
                else:
                    ans_arr.append([nums[x], nums[lp], nums[rp]])
                    while lp < rp and nums[lp] == nums[lp+1]:
                        lp +=1
                    
                    lp += 1
                    rp -= 1

        return ans_arr
        
