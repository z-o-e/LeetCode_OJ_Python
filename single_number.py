class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        xor = 0
        for elem in A:
            xor ^= elem
        return xor