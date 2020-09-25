
#간단한 다익스트라 알고리즘

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())

#간선정보,방문여부,거리합계를 나타내는 리스트 생성 -> 노드번호를 인덱스로 접근할 수 있음
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

#간선의 정보를 그래프에 담는다.
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):

    #현재 시작노드이므로 거리=0, 방문여부는 True로 초기화
    distance[start]=0
    visited[start]=True

    #현재 노드의 간선정보에서 (이동하려는 노드, 비용) 이동하려는 노드들의 거리합계에 비용을 넣는다.
    for j in graph[start]:
        distance[j[0]]=j[1]

    #다음 노드를 모두 순회한다. 이미 하나의 노드는 했으므로 n-1만큼 순회
    for i in range(n-1):
        #함수호출->다음 노드를 선택한다.
        now=get_smallest_node()
        visited[now]=True

        #현재 노드의 간선정보에서 (이동하려는 노드, 비용) 이동하려는 노드들의 거리합계에 비용을 추가한다.
        for j in graph[now]:
            cost=distance[now]+j[1]
            #계산한 비용이 원래있던 비용보다 작을때 치환한다.
            if cost<distance[j[0]]:
                distance[j[0]]=cost

def get_smallest_node():
    min_value=INF
    index=0

    #모든 노드를 돌며 거리합계가 가장 짧은거 선택(거리가 같다면 숫자가 작은것부터)
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i

    return index

dijkstra(start)

print(distance)