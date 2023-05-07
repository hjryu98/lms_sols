## template
def front(x):
    ans = 0
    if x < arr[0]:
        return -1
    else:
        if x == arr[0]:
            return 0

    s = 0
    e = n - 1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < x:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1

    if arr[ans] != x:
        return -1
    else:
        return ans


def rear(x):
    ans = 0
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] <= x:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    if arr[ans] == x:
        return ans
    else:
        return -1


n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
query = list(map(int, input().split()))

for i in range(len(query)):
    val = query[i]
    f = front(val)
    r = rear(val)
    if f == -1 or r == -1:
        print(0)
    else:
        print(r - f + 1)

