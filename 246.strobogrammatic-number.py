class Solution(object):
    #T: N/2
    #S: 1
    def isStrobogrammatic(self, num):
        map_arr = {
            "0":"0",
            "1":"1",
            "8":"8",
            "6":"9",
            "9":"6",
        }
        for i in range(len(num)/2+1):
            start = num[i]
            end = num[-i-1]
            if start in map_arr:
                if not map_arr[start] == end:
                    return False
            else:
                return False
        return True
