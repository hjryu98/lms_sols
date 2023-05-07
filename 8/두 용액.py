## template
n = int(input())
ans = 1e14
small = 0
big = 0

arr = list(map(int, input().split()))
arr.sort()

s = 0
e = n - 1

while s < e:
    val = arr[s] + arr[e]
    if val < 0:
        if ans > abs(val):
            small = arr[s]
            big = arr[e]
            ans = abs(val)
        s += 1

    elif val > 0:
        if ans > val:
            small = arr[s]
            big = arr[e]
            ans = val
        e -= 1

    else:
        small = arr[s]
        big = arr[e]
        break

print("{} {}".format(small, big))