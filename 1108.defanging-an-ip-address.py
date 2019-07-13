class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #t: O(n)
        #s: O(n)
        ans_str = ""
        for k, v in enumerate(address):
            #print(k, v)
            if v == ".":
                #print (v)
                v = "[.]"
            
            ans_str += v
        return ans_str
