#python3
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        if x <= 2:
            return 1
        
        for i in range(2, x):
            if i*i == x:
                return i
            else:
                if i*i > x:
                    return i - 1
