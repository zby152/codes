S=input()
T=input()

i=0
j=0
temp=T[0]
while j<len(S):
    if S[j]==temp:
        j+=1
        i+=1
        temp=T[i]
    else:
        j+=1

print(i)
    
    
