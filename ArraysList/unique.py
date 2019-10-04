#check if string has all unique characters

def checkUnique(str):
    unique = {}
    
    for i in str:
        unique.setdefault(i, 0)
        unique[i] += 1

    uniqueValues = unique.values()

    for j in uniqueValues:
        if(j > 1):
            return print(str + ' - is not unique')  

    print(str + ' - is unique')


checkUnique("asdads")
checkUnique("asr")
