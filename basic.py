
# 화성탐사
# 다익스트라 힙

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

import heapq
import sys

input=sys.stdin.readline
INF=987654321

#오른/밑/왼/위
dx=[1,0,-1,0]
dy=[0,1,0,-1]

t=int(input())

for _ in range(t):
    graph=[]
    n=int(input())
    for _ in range(n):
        nlist=list(map(int,input().split()))
        graph.append(nlist)

print(graph)