class Solution:
    def inverted_triangle(self, rows: int):
        for i in range(rows):
            space = ' ' * i
            stars = '*' * (2*(rows-i) -1)
            print(space + stars)
            
if __name__=="__main__":
    s = Solution()
    s.inverted_triangle(5)