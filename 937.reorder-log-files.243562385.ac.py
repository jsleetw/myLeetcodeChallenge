class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        return sorted(logs, key=self.f)

    def f(self, letter_arr):
        id_, rest = letter_arr.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1, )
    
