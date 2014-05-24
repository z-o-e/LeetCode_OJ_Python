class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        head = l = 0
        ss = ''
            
        for i in range(len(s)):
            if s[i] not in ss:
                ss += s[i]
            else:
                if i - head  > l:
                    l = i - head 
                head = head + ss.index(s[i]) + 1
                ss = s[head: i+1]
        
        # length of last ss is probably not accounted for l
        return max(len(ss),l)
           