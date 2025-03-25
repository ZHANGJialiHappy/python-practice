from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        if numRows ==0:
            return output
        
        if numRows==1:
            first_row=[1]
            output.append(first_row)
            return output
         
        if numRows==2:  
            first_row=[1]  
            second_row=[1,1]
            output.append(first_row)
            output.append(second_row)
            return output
        
        if numRows>2:  
            first_row=[1]  
            second_row=[1,1]
            output.append(first_row)
            output.append(second_row)      
            for i in range(1, numRows-1):
                pre_row=output[i]
                current_row=[1]
                
                for j in range(0,i):
                    current_row.append(pre_row[j]+pre_row[j+1])
                
                current_row.append(1)
                output.append(current_row)
            
        return output
    
if __name__=="__main__":
    s=Solution()
    print(s.generate(1))
            
            
        