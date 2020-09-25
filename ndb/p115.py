
# 왕실의 나이트

#현재 위치 입력받기
point=input()

column=ord(point[0])-ord("a")+1
row=int(point[1])

#이동가능한 전체 경로
steps=[(-2,+1),(-2,-1),(-1,-2),(+1,-2),(+2,+1),(+2,-1),(-1,+2),(+1,+2)]

count=0

for s in steps:
    ncolumn=column+s[0]
    nrow=row+s[1]
    if 0<ncolumn<9 and 0<nrow<9 :
        count+=1
print(count)


