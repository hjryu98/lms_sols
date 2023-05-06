a, b = map(int, input().split())
ans = 0
mx = -1
mn = 1e12
idx = 1

while idx * idx <= b:
    if idx * idx >= a:
        mn = min(idx * idx, mn)
        mx = max(idx * idx, mx)
        ans += idx * idx
    idx += 1

if ans == 0:
    print(-1)
else:
    print(ans)
    print("{} {}".format(mn, mx))