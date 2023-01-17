def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        rn = [str(i) for i in str(s)]
        print(rn)
        n = 0
        for i in rn:
            if i == "I":
                n += 1
            if i == "V":
                n += 5
            if i == "X":
                n += 10
            if i == "L":
                n += 50
            if i == "C":
                n += 100
            if i == "D":
                n += 500
            if i == "M":
                n += 1000
        return n
print(romanToInt("III"))