def suffix_array(s):
    n = len(s)
    sa = [i for i in range(1, n + 1)]
    rk = [ord(c)-ord("a")+1 for c in s]
    rk.extend([0 for _ in range(n)])

    w = 1
    while w < n:
        sa.sort(key=lambda x: (rk[x], rk[x + w]))
        oldrk = rk.copy()
        p = 0
        for i in range(n):
            if oldrk[sa[i]] == oldrk[sa[i - 1]] and (sa[i] + w < n and oldrk[sa[i] + w] == oldrk[sa[i - 1] + w]):
                rk[sa[i]] = p
            else:
                p += 1
                rk[sa[i]] = p
        w <<= 1

    return sa

# Example usage:
s ="aabaaaab"
sa = suffix_array(s)
for i in sa:
    print(i, end=' ')