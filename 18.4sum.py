class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        #use pairs
        allPairSum = {}
        nums.sort()
        #print(nums)
        for i in range(1, len(nums)):
            for right in range( i+1 , len(nums)):
                sum = nums[i] + nums[right]
                diff = target - sum
                if diff in allPairSum:
                    for pair in allPairSum[diff]:
                        fourPair = pair + [ nums[i], nums[right] ]
                        if fourPair not in ans:
                            ans.append(fourPair)
            for left in range(0, i):
                sum = nums[i] + nums[left]
                #print(sum)
                if sum in allPairSum:
                    allPairSum[sum].append( [ nums[left], nums[i] ] )
                else:
                    allPairSum[sum] = [ [ nums[left], nums[i] ] ]


        #print(allPairSum)
        #print(ans)
        ans.sort()
        return ans
