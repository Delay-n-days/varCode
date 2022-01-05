def tuofeng(str1):
    Arrstr = str1.split("\n")
    a = ""
    for str in Arrstr:
        ArrS = str.split(" ")
        for s in ArrS:
            s = s.capitalize()
            a +=s
        a += "\n"
    return a
print(tuofeng("I love you\nyou love me"))