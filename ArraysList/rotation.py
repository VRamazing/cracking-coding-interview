def rotation(str1, str2):
    if(len(str1) != len(str2)):
        return False
    
    tempStr = str1 + str1
    if(tempStr.find(str2)>0):
        return True
    return False


print(rotation("ABCD", "CDAB"))
print(rotation("ABCD", "ABDC"))

