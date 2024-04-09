(N, M) = map(int, input().split())

print("┌─", end='')
for _ in range(M - 1):
    print("┬─", end='')
print("┐")

for _ in range(N - 1):
    print("│", end='')
    for _ in range(M):
        print("  │", end="")
    print()

    print("├", end='')
    for _ in range(M - 1):
        print("─┼", end="")
    print("─┤", end='')
    print()

print("│", end='')
for _ in range(M):
    print("  │", end="")
print()

print("└─", end='')
for _ in range(M - 1):
    print("┴─", end='')
print("┘")
