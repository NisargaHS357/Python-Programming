str=input()
start,length=map(int,input().split())
ans=" "
for i in range(start,len(str)):
    ans=ans+str[i]
    if len(ans)==length:
        break
    print(ans)