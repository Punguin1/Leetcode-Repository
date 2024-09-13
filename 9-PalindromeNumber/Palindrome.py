class Solution(object):
    def isPalindrome(self, x):
        ls = list(str(x))
        return ls == ls[::-1]
        
