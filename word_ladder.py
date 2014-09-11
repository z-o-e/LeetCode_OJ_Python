class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if len(start)!=len(end) or len(start)==0:
            return 0
            
        lenWord = len(start)
        # deque (double-ended) for generalizationg of stacks, queues
        q = collections.deque([(start, 1)])
        
        # BFS
        while q:
            cur = q.popleft()
            curWord, level = cur[0], cur[1]
            
            if curWord==end:
                return level
                
            for i in range(lenWord):
                before, after = curWord[:i], curWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = before+j+after
                    if newWord==end:
                        return level+1
                    elif newWord in dict:
                        q.append((newWord,level+1))
                        dict.remove(newWord)
                        
        return 0