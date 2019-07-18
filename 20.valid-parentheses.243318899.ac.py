class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        map = {
                ")" : "(",
                "}" : "{",
                "]" : "[",
                }
        #use stack
        stack = []

        for char in s:
            if char in map:
                if stack:
                    top_element = stack.pop() 
                else:
                    top_element = "#"

                if top_element != map[char]:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
