
#백준 알고리즘 1874 [스택수열]

#수열을 만들 숫자 입력받기
n=int(input())
nth=0
result=''
numlist=[]
wishlist=[]

for _ in range(n):
    wishlist.append(int(input()))

for i in range(1,n+1):
    numlist.append(i)
    result+="+"
    while len(numlist)!=0:
        if wishlist[nth]==numlist[-1]:
            numlist.pop()
            result+="-"
            nth+=1
        else:
            break

if len(result)==n*2:
    for i in result:
        print(i)
else:
    print("NO")

