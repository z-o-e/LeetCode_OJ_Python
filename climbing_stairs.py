class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self,n):
		prev = 0
		cur = 1
		for i in range(n):
			tmp = cur
			cur = cur+prev
			prev = tmp
		return cur
