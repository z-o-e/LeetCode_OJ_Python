class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        sp = path.split('/')
        for s in range(sp.count('')):
            sp.remove('')
        for t in range(sp.count('.')):
            sp.remove('.')

        res=''
        counter = 0
        for i in range(len(sp)-1,-1,-1):
            if sp[i]=='..':
                counter += 1
                continue
            if counter == 0:
                res = '/'+sp[i] + res
            else:
                counter -= 1
                
        if res=='':
            return 
            
        return res