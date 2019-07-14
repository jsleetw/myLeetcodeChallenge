class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #time: O(n)
        #space: O(n)
        #trying to write code readable not quickly
        
        email_list = []
        
        for i in emails:
            str_arr = i.split("@")
            name = str_arr[0]
            domain = str_arr[1]
            if "+" in name:
                name_arr = name.split("+")
                real_name = name_arr[0].replace(".","")
            else:
                real_name = name.replace(".","")
            
            email = real_name+"@"+domain
            if email not in email_list:
                email_list.append(email)
                
        return len(email_list)
                
                
            
