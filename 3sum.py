class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = []
        if len(num) < 3:
            return res
            
        Slen, Snum= len(num), sorted(num)    
        
        for i in range(Slen-2):
            # unique
            if i==0 or Snum[i] > Snum[i-1]:
                j = i+1
                k = Slen-1
                
                while (j<k):
                    if -Snum[i] == Snum[j] + Snum[k]:
                        res.append([Snum[i] , Snum[j] , Snum[k]])
                        j += 1
                        k -= 1
                        # avoid duplicate
                        while j<k and Snum[j]==Snum[j-1]:
                            j += 1
                        while j<k and Snum[k]==Snum[k+1]:
                            k -= 1
                    elif -Snum[i] > Snum[j] + Snum[k]:
                        j += 1
                    else:
                        k -= 1
            
        return res