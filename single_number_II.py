class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        n,flag = len(A),0
        if not n:
            return n
            
        count = [0]*32
        res = 0
        
        for i in range(32):
            for j in range(n):
                if (abs(A[j])>>i) & 1:
                    count[i] = (count[i]+1)%3
                if A[j]<0:
                    flag += 1
                    
            res |= (count[i]<<i)
        
        if not flag%3:
            flag = 1
        else:
            flag = -1
        
        return res*flag