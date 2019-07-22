class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        domain_count_arr = {}
        
        for i in cpdomains:
            cpdomain_arr = i.split(" ")
            count = int(cpdomain_arr[0])
            domain = cpdomain_arr[1]
            domain_arr = domain.split(".")
            full_domain = ""
            for domain in reversed(domain_arr):
                if(full_domain):
                    full_domain = domain+"."+full_domain
                else:
                    full_domain = domain
                
                if(full_domain not in domain_count_arr):
                    domain_count_arr[full_domain] = count
                else:
                    domain_count_arr[full_domain] += count
        
        ret_list = []
        for key, value in domain_count_arr.items():
            ret_list.append(str(value)+" "+key)
        
        return(ret_list)
