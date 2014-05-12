class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):

        res, Smap = [], {}
        
        Slen, Snum = len(num), sorted(num)
        
        if Slen<4:
            return res
            
        for i in range(Slen-1):
            for j in xrange(i+1,Slen):
                if Smap.has_key(Snum[i]+Snum[j]):
                    Smap[Snum[i]+Snum[j]].append([i,j])
                else:
                    Smap[Snum[i]+Snum[j]]=[[i,j]]

        for small in Smap:
            if target-small in Smap:
                for (a,b) in Smap[small]:
                    for (c,d) in Smap[target-small]:
                        if a!=d and a!=c and b!=c and b!=d:
                            tmp = sorted([Snum[a],Snum[b],Snum[c],Snum[d]])
                            if tmp not in res:
                                res.append(tmp)
        
        return sorted(res)
                    