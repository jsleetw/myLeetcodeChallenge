class Solution(object):

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #return self.bub_sort(nums)
        return self.merge_sort(nums)
        #return sorted(nums)
    
    #t: n log n
    def merge_sort(self, nums):
        #split array to min 1
        if len(nums) <=1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        #print(left, right)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self.merge(left, right)
        
    def merge(self, left, right):
        res = []
        #print(left, right)
        while left and right:
            if left[0] <= right[0]:
                res.append( left.pop(0) )
            else:
                res.append( right.pop(0) )
        #print('#')
        #print(res)
        
        if left:
            res += left
        if right:
            res += right
        
        #print(res)
        return res
        
        
    #bubsort t= O(n^2)
    def bub_sort(self, nums):
        list_len = len(nums)
        for i in range(list_len-1):
            for j in range(list_len-1, i, -1):
                if nums[j -1]> nums[j]:
                    #print(nums[j -1], nums[j])
                    #swap
                    nums[j-1], nums[j] = nums[j], nums[j -1]
                    #print(nums)
        return nums
