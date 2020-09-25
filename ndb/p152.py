
#괴물을 피해 미로를 탈출하기

from collections import deque

#미로 크기 입력받기
n,m=map(int,input().split())
#미로 상태 입력받기(2차원 배열)
miro=[]
for _ in range(n):
    miro.append(list(map(int,input())))

#이동 방향벡터 정의(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    #경로를 담을 큐 선언
    queue=deque()
    queue.append((x,y))

    #큐가 빌때까지 반복
    while queue:
        print(queue)
        #제일 앞에있는 큐 꺼내서 확인
        x,y=queue.popleft()
        #현재위치에서 네방향 상태 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #맵을 벗어나는 경우는 패스
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #괴물이 있는 자리는 패스
            if miro[nx][ny]==0:
                continue
            #갈 수 있는 위치라면, 이동한 후 숫자 1 증가시키기
            if miro[nx][ny]==1:
                miro[nx][ny]=miro[x][y]+1
                queue.append((nx,ny))
    return miro[n-1][m-1]

print(bfs(0,0))


