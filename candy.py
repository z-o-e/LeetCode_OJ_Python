class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1]*len(ratings)
        
        # if len(ratings)==2 and ratings[0]!=ratings[1]:
        #     return 3
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1
                
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])
                
        total=0
        for c in candies:
            total+=c
                
        return total