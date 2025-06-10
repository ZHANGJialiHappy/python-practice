class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=[]
        while columnNumber>0:
            columnNumber-=1
            result.append(chr((columnNumber%26)+ord('A')))
            columnNumber//=26
            
        return ''.join(reversed(result))
    
if __name__=='__main__':
    s=Solution()
    print(s.convertToTitle(701))
