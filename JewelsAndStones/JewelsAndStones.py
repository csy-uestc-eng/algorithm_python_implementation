class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        if J == "" or S == "":
            return count
        for c in J:
            count += S.count(c)
            S.strip(c)
        return count
