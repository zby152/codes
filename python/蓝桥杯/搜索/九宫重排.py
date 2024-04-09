from collections import deque

direc = [3, -3, 1, -1]


def inlaw(p,n_p):
    if n_p > 8 or n_p < 0:
        return False
    if p==2 and n_p==3:
        return False
    if p==5 and n_p==6:
        return False
    if p==3 and n_p==2:
        return False
    if p==6 and n_p==5:
        return False
    else:
        return True


start = list(input())
end = list(input())

q = deque()
p = start.index(".")
q.append([start, 0,p])
start_s="".join(start)
vis={start_s:1}
ans = 0

while len(q) > 0:
    state, step ,p= q.popleft()
    if state == end:
        ans = step
        break

    for di in direc:
        n_p = p + di
        if inlaw(p,n_p) :
            n_state = state.copy()
            n_state[p], n_state[n_p] = state[n_p], state[p]
            state_s="".join(n_state)
            if state_s not in vis:
                q.append([n_state, step + 1,n_p])
                vis[state_s]=1

print(ans)
