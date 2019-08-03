class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans_list = []
        for i in nums1:
            if i in nums2:
                ans_list.append(i)
                nums2.remove(i)
        
        return ans_list
