def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        p1 = [str(i) for i in str(x)]
        p2 = p1[:]
        p2.reverse()
        if p1 == p2:
            return True
        else:
            return False 
print(isPalindrome(-121))