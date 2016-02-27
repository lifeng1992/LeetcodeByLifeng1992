class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        re = sys.modules["re"]
        patternA = re.compile(r" *[+-]?\d+.*")
        patternB = re.compile(r"[+-]?\d+")
        
        if(patternA.match(str) == None):
            return 0
        else:
            strA = patternB.findall(str)[0]
            if(strA[0] == "+"):
                x = int(strA[1:])
            elif(strA[0] == "-"):
                x = -1 * int(strA[1:])
            else:
                x = int(strA)
                
        if(x >= pow(2, 31)):
            return pow(2, 31) - 1
        elif(x <= -1*pow(2, 31)):
            return -1*pow(2, 31)
        else:
            return x