from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m-1
        point2 = n-1
        point_array = m + n - 1

        while point2 >= 0:
            if point1 >=0 and nums1[point1]> nums2[point2]:
                nums1[point_array] = nums1[point1]
                point1-=1
            else:
                nums1[point_array] = nums2[point2]
                point2 -=1
            point_array-=1
        print(nums1)

if __name__ == "__main__":
    solution = Solution()
    solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

