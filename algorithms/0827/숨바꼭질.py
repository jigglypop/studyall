from collections import deque

N,K = map(int,input().split())
Max = 10**5
D = [-1]*(Max+1)
D[N] = 0
Q = deque()
Q.append(N)
while Q:
    x = Q.popleft()
    for nx in [x-1,x+1,2*x]:
        if 0 <= nx <= Max and D[nx] == -1:
            Q.append(nx)
            D[nx] = D[x]+1
print(D[K])

