class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans_str = ""
        for k, v in enumerate(address):
            #print(k, v)
            if v == ".":
                #print (v)
                v = "[.]"
            
            ans_str += v
        return ans_str
