from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(1, rowIndex+1):
            result.append(result[-1]*(rowIndex -i+1)//i)
        return result
    
if __name__ == "__main__":
    s=Solution()
    print(s.getRow(4))