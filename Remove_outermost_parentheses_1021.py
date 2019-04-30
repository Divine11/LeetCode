def removeOuterParentheses(S):
    count = 0
    result = []
    temp = []
    #print(S)
    for i in S:
        if i=='(':
            if count!=0:
                temp.append(i)
            count+=1
        else:
            count-=1
            if count!=0:
                temp.append(i)
        if count==0:
            #print(temp)
            result.append(''.join(temp))
            temp = []
            
    return ''.join(result)
