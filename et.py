
class Solution(object):
    def sortedSquares(self, nums):
        n=[]
        for i in nums:
            n.append(i*i)
        return sorted(n)
