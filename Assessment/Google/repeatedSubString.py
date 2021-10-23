str1 = 'ababc'


def repeatedSubString(str1):
    if not str1:
        return False
    str2 = (str1 + str1)[1:-1]
    return str2.find(str1)!=-1


print(repeatedSubString(str1))

