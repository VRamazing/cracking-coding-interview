def stringCompression(str1):
    counter=0
    prevChar = str1[0]
    str2=""
    charChanged = False
    loopCounter = 0
    
    for char in str1:
        if(char==prevChar):
            counter+=1
            charChanged = False
        else:
            str2 += prevChar + str(counter)
            counter=1
            prevChar = char
            if(loopCounter == len(str1) - 1):
                str2 += prevChar + str(counter)
            charChanged = True
        loopCounter+=1
    if(not charChanged):
        str2+= prevChar + str(counter)
    
    return str2


print(stringCompression("a"))
print(stringCompression("aaabbbccc"))
print(stringCompression("aabbccaadd"))
print(stringCompression("aabccdeee"))
print(stringCompression("aabccdeef"))
print(stringCompression("abc"))
