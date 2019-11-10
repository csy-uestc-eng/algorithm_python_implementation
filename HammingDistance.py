class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        xy = x ^ y
        str_xy = bin(xy)[2:]
        return str_xy.count('1')
