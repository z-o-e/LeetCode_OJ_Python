class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        flag = 1
        if dividend < 0:
            dividend *= -1
            flag *= -1
        if divisor < 0:
            divisor *= -1
            flag *= -1
        
        res = 0
        while divisor <= dividend:
            dividend -= divisor
            res += 1
            tmp = divisor << 1
            k = 1
            while tmp <= dividend:
                dividend -= tmp
                tmp <<= 1
                k <<= 1
                res += k
        
        return flag*res
            