#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
queue <int> q;
int n, k, arr[100002];
int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n);

    q.push(arr[0]);

    for (int i = 1; i < n; i++) {
        int cur = arr[i];

        if (q.front() + k < cur) {
            q.pop();
        }
        q.push(cur);
    }
    cout << q.size();

    return 0;
}