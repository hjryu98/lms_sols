## template
t = int(input())
arr = []
pref = []
pref.append(0)
for i in range(1, 1001):
    for _ in range(i):
        arr.append(i)

for i in range(1, 5051):
    pref.append(pref[i - 1] + arr[i - 1])

for i in range(1, t + 1):
    s, e = map(int, input().split())
    print("#{} {}".format(i, pref[e] - pref[s - 1]))
