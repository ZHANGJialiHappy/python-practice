from typing import List
class Solution:
    def find_max(self, nums:List[int]) -> int:
        max=nums[0]
        for num in nums:
            if num > max:
                max = num
        return max
    
if __name__ == '__main__':
    nums = [5,100,2,-10]
    s = Solution()
    print(s.find_max(nums))