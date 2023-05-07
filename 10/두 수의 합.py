## template
n, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
s = 0
e = n - 1
ans = 0
while s < e:
    val = arr[s] + arr[e]

    if val > k:
        e -= 1
    elif val < k:
        s += 1
    else:
        s += 1
        ans += 1

print(ans)
