n=int(input())
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for _ in range(n):
    RC=input()
    index=1
    num_str=""
    while index<len(RC) and RC[index].isdigit():
        num_str=num_str+RC[index]
        index+=1
    R=int(num_str)
    
    num_str=""
    index+=1
    while index<len(RC) :
        num_str=num_str+RC[index]
        index+=1
    C=int(num_str)

    result=""
    if C<=26:
        result=result+letters[C-1]
    else:
        result=result+letters[C//26-1]
        result=result+letters[C%26-1]
    result=result+str(R)
    print(result)
