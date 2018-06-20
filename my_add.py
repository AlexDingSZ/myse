def add (a,*listb, **dictc):
    sumb =0
    for i in listb:
        sumb= sumb +i
    sumc = 0
    for i in dictc:
        sumc = sumc + dictc[i]
    result = a + sumb + sumc
    return result

listb = (1,4,6)
dictc = {"aa":10,"bb":20}
result2=add(5,*listb, **dictc)
print(result2)
