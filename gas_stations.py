class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        stations = len(gas)
        
        diff = [0]*stations
        
        for i in range(stations):
            diff[i] = gas[i] - cost[i]
        
        total, subtotal, startnode = 0, 0, 0
        
        for i in range(stations):
            total += diff[i]
            
            subtotal += diff[i]
            
            if subtotal < 0:
                # cannot be startnode, reset 
                subtotal = 0
                startnode = i + 1
            
        if total < 0:
            return -1
            
        return startnode