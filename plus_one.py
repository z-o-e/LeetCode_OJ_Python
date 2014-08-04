class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits[-1], carry = (digits[-1]+1)%10, (digits[-1]+1)//10
        idx = len(digits)-2
        
        while carry!=0:
            if idx >=0:
                digits[idx], carry = (digits[idx]+carry)%10, (digits[idx]+carry)//10
                idx -= 1
            else:
                digits, carry = [1]+digits, 0
                
        return digits