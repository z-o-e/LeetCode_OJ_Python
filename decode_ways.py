 # somewhat similar to Fibonacci
 # transition function f
 # f[n]=f[n-1]+f[n-2]   s[n] is valid && s[n-1]s[n] is valid 
 # f[n] = f[n-1]        s[n] is valid && s[n-1]s[n] is unvalid
 # f[n] = f[n-2]        s[n] is unvalid && s[n-1]s[n] is valid
 # f[n]=0               s[n] is unvalid && s[n-1]s[n] is unvalid
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        sLen = len(s)
        if sLen==0 or s[0]=='0':
            return 0
        
        f = [0]*(sLen+1)
        f[0], f[1] = 1, 1 
        
        for i in range(2,sLen+1):
            if int(s[i-1])>0:
                if int(s[i-2:i])<27 and int(s[i-2:i])>9:
                    f[i] = f[i-1]+f[i-2]
                else:
                    f[i] = f[i-1]
            else:
                if int(s[i-2:i])<27 and int(s[i-2:i])>9:
                    f[i] = f[i-2]
                else:
                    f[i]=0
        return f[-1]