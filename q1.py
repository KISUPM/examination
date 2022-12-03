# example input
arrayA = ["Jan"   ,"Feb"  ,"Jan"  ,"Apr"  ,"Mar"  ,"Apr"  ,"May"  ,"Apr"]
arrayB = [10      ,20     ,30     ,40     ,50     ,60     ,70     ,70]

def combine(arrayA,arrayB):
    result = []
    temp = {}
    temp2 = {}
    for i in range(len(arrayA)):
        try:
            temp[arrayA[i]]+=arrayB[i]
        except:
            temp[arrayA[i]]=arrayB[i]

    for i in temp.keys():
        temp2["Month"] = i
        temp2["Sum Value"] = temp[i]
        result.append(temp2)
    print(result)
    # return result

combine(arrayA,arrayB)