class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        delta = 10000000
        
        Slen, Snum = len(num), sorted(num)
        
        for i in range(Slen-2):
            j = i+1
            k = Slen - 1
            
            while j<k :
                tmp = target - Snum[i]- Snum[j]- Snum[k]
                if abs(tmp)<delta:
                    res = Snum[i]+ Snum[j]+ Snum[k]
                    delta = abs(tmp)
                
                if tmp<0:
                    k -= 1
                elif tmp>0:
                    j += 1
                else:
                    return sol
                    
        return res