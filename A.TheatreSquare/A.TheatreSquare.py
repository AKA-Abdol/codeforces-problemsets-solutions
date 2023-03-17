def ceil(m):
    if m != int(m):
        return int(m) + 1
    else:
        return int(m)

n, m, a = map(int, input().split())
print(ceil(m / a) * ceil(n / a))