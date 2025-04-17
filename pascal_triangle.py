from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        if numRows ==0:
            return output
        
        first_row=[1]
        output.append(first_row)
         
        for i in range(1, numRows):
            pre_row=output[i-1]
            current_row=[1]
            
            for j in range(1,i):
                current_row.append(pre_row[j-1]+pre_row[j])
            
            current_row.append(1)
            output.append(current_row)
            
        return output
    
if __name__=="__main__":
    s=Solution()
    print(s.generate(5))
            
            
        