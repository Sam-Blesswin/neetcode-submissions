class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r = 0,m-1
        row=0
        while l<=r:
            mid = (l+r)//2
            if (matrix[mid][0] <= target) and (target <= matrix[mid][n-1]):
                row=mid
                break
            elif target < matrix[mid][0]:
                r=mid-1
            else:
                l=mid+1

        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid-1
            else:
                l = mid+1
        
        return False
