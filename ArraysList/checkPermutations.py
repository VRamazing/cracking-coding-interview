
def checkPermutations(str1, str2):
    uniqueStr1Dict = outputUniqueDict(str1)
    uniqueStr2Dict = outputUniqueDict(str2)
    

def outputUniqueDict(str):
    unique = {}
    
    for i in str:
        unique.setdefault(i, 0)
        unique[i] += 1
    
    return unique
    


checkUnique("asdads")
checkUnique("asr")
