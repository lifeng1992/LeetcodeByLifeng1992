class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(abs(x)>pow(2, 31)):
            return 0
        else:
            if(x>0):
                y = int(str(x)[::-1])
            else:
                y = -1*int(str(-x)[::-1])
        
        if(abs(y)>pow(2, 31)):
            return 0
        else:
            return y
