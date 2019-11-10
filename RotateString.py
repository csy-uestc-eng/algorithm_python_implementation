class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not all([A, B]):
            return A == B
        if len(A) != len(B):
            return False
        pos = B.rfind(A[0])
        while pos != -1:
            if self.isRotate(A, B, pos):
                return True
            pos = B.rfind(A[0],0, pos-1)

    def isRotate(A, B, pos):
        pass

    def rotateString01(self, A, B):
        if not all([A, B]):
            return A == B
        if len(A) != len(B):
            return False
        for i in range(0, len(A)):
            head = A[0]
            A = A[1:] + head
            if A == B:
                return True
        return False

