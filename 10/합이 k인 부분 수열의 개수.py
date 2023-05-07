## template
n, k = map(int, input().split())

arr = list(map(int, input().split()))

s = 0
e = 0
ans = 0
val = arr[s]

while e <= n - 1 and s <= e:
    if val < k:
        e += 1

        if e == n:
            break

        val += arr[e]
    elif val > k:
        val -= arr[s]
        s += 1
    else:
        ans += 1
        val -= arr[s]
        s += 1

print(ans)