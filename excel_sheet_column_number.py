class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        length=len(columnTitle)
        for i in range(0, length):
            result+=(ord(columnTitle[i])-64)*pow(26,(length-i-1))
            
        return result
    
if __name__=='__main__':
    s=Solution()
    print(s.titleToNumber("ZY"))