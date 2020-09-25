
#얼음틀 얼음개수 세기

#얼음틀 크기
n,m=map(int,input().split())
#얼음틀 상태 입력 (2차원 배열 생성)
ice=[]
for _ in range(n):
    ice.append(list(map(int,input())))

#DFS 알고리즘 정의
def dfs(x,y):
    if 0>x or x>=n or 0>y or y>=m:
        return False
    if ice[x][y]==0:
        ice[x][y]=1 #방문체크
        #현재위치의 상하좌우에 연쇄적으로 주변 탐색 (재귀함수)
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

#얼음틀 모든 위치 탐색
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)

