from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        m= defaultdict(int)

        for num in nums:
            m[num] +=1

        for key, value in m.items():
            if value > n/2:
                return key
    
    def majorityElement2(self, nums: List[int]) -> int:
        count=1
        candidate=nums[0]

        for num in nums[1:]:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count -=1
        return candidate

if __name__=="__main__":
    solution = Solution()
    print(solution.majorityElement2([2,2,1,1,1,2,2]))
