T=int(input())

def find_same(a,b,c,d,e,f):
    if (a==c and a==e) or (a==c and a==f):
        return True
    if (a==d and a==e) or (a==d and a==f):
        return True
    if (b==c and b==e) or (b==c and b==f):
        return True
    if (b==d and b==e) or (b==d and b==f):
        return True
    return False

def check1(a,b,c,d,e,f):
    box1=[a,b]
    box2=[c,d]
    box3=[e,f]
    flag=8
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if box1[i]==box2[j]+box3[k]:
                    if box2[(j+1)%2]==box3[(k+1)%2]:
                        return 4
                    else:
                      flag=6

                if box2[j]==box1[i]+box3[k]:
                    if box1[(i+1)%2]==box3[(k+1)%2]:
                        return 4
                    else:
                        flag=6
                

                if box3[k]==box1[i]+box2[j]:
                    if box1[(i+1)%2]==box2[(j+1)%2]:
                        return 4
                    else:
                      flag=6
    return flag

def check2(a,b,c,d,e,f):
    box1=[a,b]
    box2=[c,d]
    box3=[e,f]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if box1[i]==box2[j] or box2[j]==box3[k] or box1[i]==box3[k]:
                    return 6
    return 8
        

for _ in range(T):
    flag=8
    a1,b1,a2,b2,a3,b3=map(int,input().split())
    if find_same(a1,b1,a2,b2,a3,b3):
        flag=4
    flag=min(flag,check1(a1,b1,a2,b2,a3,b3))
    flag=min(flag,check2(a1,b1,a2,b2,a3,b3))

    print(flag)
        
    
        
