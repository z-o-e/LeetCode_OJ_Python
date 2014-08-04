class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        idxA, idxB, idx = len(a)-1, len(b)-1, max(len(a),len(b))-1
        res= [0]*(idx+1)
        carry = 0
        
        while idx>=0:
            if idxA<0:
                res[idx], carry = str((int(b[idxB])+carry)%2), (int(b[idxB])+carry)//2
                idx -= 1
                idxB -= 1
            elif idxB<0:
                res[idx], carry = str((int(a[idxA])+carry)%2), (int(a[idxA])+carry)//2
                idx -= 1
                idxA -= 1
            else:
                res[idx], carry = str((int(b[idxB])+int(a[idxA])+carry)%2), (int(b[idxB])+int(a[idxA])+carry)//2
                idx -= 1
                idxA -= 1
                idxB -= 1
                
        if carry!=0:
            return "1"+"".join(res)
            
        return "".join(res)