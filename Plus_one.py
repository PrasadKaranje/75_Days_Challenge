class Solution(object):
    def plusOne(self, digits):
        ls=list()
        num = "".join(map(str,digits))
        num = int(num)+1
        #num =str(num)
        for i in str(num):
            ls.append(int(i))
        return ls
