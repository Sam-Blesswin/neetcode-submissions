class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res=[]
        rs,re = 0,m-1
        cs,ce = 0,n-1

        while rs<=re and cs<=ce:
            for j in range(cs, ce+1):
                res.append(matrix[rs][j])
            rs+=1
            for i in range(rs, re+1):
                res.append(matrix[i][ce])
            ce-=1
            if rs > re or cs > ce:
                break
            for j in range(ce,cs-1,-1):
                res.append(matrix[re][j])
            re-=1
            for i in range(re,rs-1,-1):
                res.append(matrix[i][cs])
            cs+=1
        return res


        