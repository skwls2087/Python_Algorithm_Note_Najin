
#맵 크기 지정하기
n,m=map(int,input().split())
#현재위치와 방향 입력받기
x,y,dir=map(int,input().split())
#맵 형태 입력받기
gmap=[]
for _ in range(n):
    gmap.append(list(map(int,input().split())))

#맵에서 바다인 부
smap=gmap

#방문한 맵 위 저장
gmap[x][y]=1

#방향 정의하기 (북,동,남,서)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#방향 바꾸는 함수 정의
def turn_left():
    global dir
    dir-=1
    if dir==-1:
        dir=3

count=1 #차지한 맵
turn_time=0 #회전한 횟수

#시뮬레이션 시작하기
while True:
    turn_left()
    nowx=x+dx[dir]
    nowy=y+dy[dir]

    if gmap[nowx][nowy]!=1:
        gmap[nowx][nowy]=1
        x=nowx
        y=nowy
        count+=1
        turn_time=0
    else:
        turn_time+=1

    #네 방향 다 이동할 수 없다면
    if turn_time==4:
        nowx = x - dx[dir]
        nowy = y - dy[dir]

        if smap[nowx][nowy]!=1:
            x = nowx
            y = nowy
        else:
            break
        turn_time=0

print(count)
