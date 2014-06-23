class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        ops = ["+","-","*","/"]    
        nums = []
        
        if len(tokens)==1:
            return int(tokens[0])
        
        for item in tokens:
            if item not in ops:
                nums.append(int(item))
            else:
                if item=="+":
                    nums[-2] = nums[-2] + nums[-1]
                elif item =="-":
                    nums[-2] = nums[-2] - nums[-1]
                elif item =="*":
                    nums[-2] = nums[-2] * nums[-1]
                else:
                    # to pass case eg. 6/(-132)=0, in python res=-1 
                    nums[-2] = int(1.0*nums[-2] / nums[-1])
                    
                nums.pop()
                    
        return nums[0]
