tian=["jia","yi","bing","ding","wu","ji","geng","xin","ren","gui"]
di=["zi","chou","yin","mao","chen","si","wu","wei","shen","you","xu","hai"]

year=2020
i=6
j=0

n_year=int(input())

sub=n_year-year
i=(i+sub)%10
j=(j+sub)%12

print(tian[i],end='')
print(di[j],end='')
