#  Let num = [1,2,3,...,n]. 
#  The first digit is k/(n-1)!, then let k = k % (n-1)! and remove this digit from num. 
#  The second digit is k/(n-2)!, then let k = k % (n-2)! and remove this digit from num and so on.
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res = ""
        
        num = range(n)
        k -= 1
        factorial = 1
        for i in range(1,n):
            factorial *= i
            
        for i in range(n-1, -1, -1):
            cur = num[k/factorial]
            res += str(cur)
            num.remove(cur)
            if i!=0:
                k %= factorial
                factorial /= i
            
        return res