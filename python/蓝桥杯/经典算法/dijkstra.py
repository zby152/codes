def dijkstra(start: int, mgraph: list) -> list:
    passed = [start]
    nopass = [x for x in range(len(mgraph)) if x != start]
    dis = mgraph[start]

    while len(nopass):
        idx = nopass[0]
        for i in nopass:
            if dis[i] < dis[idx]:
                idx = i

        nopass.remove(idx)
        passed.append(idx)

        for i in nopass:
            if dis[idx] + mgraph[idx][i] < dis[i]:
                dis[i] = dis[idx] + mgraph[idx][i]
    return dis


if __name__ == "__main__":
    inf = 10086
    mgraph = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf, inf, 0, 4],
              [inf, inf, inf, inf, inf, 0]]

    dis = dijkstra(0, mgraph)
    print(dis)