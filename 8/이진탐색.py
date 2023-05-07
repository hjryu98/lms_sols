## template
n, q = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

arr.sort()


def check(x):
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == x: return True
        if arr[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    return False


for i in range(q):
    val = query[i]
    if check(val) == True:
        print("YES")
    else:
        print("NO")