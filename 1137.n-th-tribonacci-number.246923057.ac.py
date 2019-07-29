"""
[1137] N-th Tribonacci Number  

https://leetcode.com/problems/n-th-tribonacci-number/description/

* algorithms
* Easy (64.14%)
* Total Accepted:    4.2K
* Total Submissions: 6.6K
* Testcase Example:  '4'

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 
Example 1:


Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4


Example 2:


Input: n = 25
Output: 1389537


 
Constraints:


	0 <= n <= 37
	The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec_p(n):
            if n is 0:
                return 0
            elif n is 1:
                return 1
            elif n is 2:
                return 1
            else:
                return (rec_p(n-1)+rec_p(n-2)+rec_p(n-3))
        
        memory = {0:0, 1:1, 2:1}
        def mem_p(n):
            if not n in memory:
                memory[n] = mem_p(n-1) + mem_p(n-2) + mem_p(n-3)
            return memory[n]
        
        def qu_p(n):
            qu = [0,1,1]
            for i in range(n-2):
                qu = qu[1:] + [sum(qu)]
            return qu[-1]

        if n is 0:
            return 0
        
        return qu_p(n)

if __name__=="__main__":
    print(Solution().tribonacci(4))
    print(Solution().tribonacci(25))