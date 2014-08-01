# if divide the solution to two parts, for each element, one part contains the element, the other don't

# for example [1,2,3]:
# recursively do
# pick 1 get [],[1]
# based on ouput of previous step pick 2 get [2], [1,2]
# based on union the previous result pick 3 get [3], [1,3], [2,3], [1,2,3]
# union again get the final result

# solution requirement the elements must be in non-decreasing order
# that means sort the input so that elements are appended in non-decreasing order

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        res, lenS = [], len(S)
        
        self.findSubsets(S, res, [], 0, lenS)
        
        return res
        
    def findSubsets(self, S, res, cur, depth, lenS):
        res.append(cur)
        if depth==lenS:
            return 
        for i in range(depth, lenS):
            tmp = []
            for item in cur:
                tmp.append(item)
            tmp.append(S[i])
            self.findSubsets(S, res, tmp, i+1, lenS)
        
        