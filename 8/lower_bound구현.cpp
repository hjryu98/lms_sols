#include <iostream>
using namespace std;
int n, q, arr[100002];

int lower_bound(int x) {
    int s = 0, e = n - 1, ans = -1;
    while (s <= e) {
        int mid = (s + e) / 2;
        if (arr[mid] < x) s = mid + 1;
        else {
            ans = mid;
            e = mid - 1;
        }
    }
    return ans;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];
    cin >> q;
    while (q--) {
        int a;
        cin >> a;
        cout << lower_bound(a) << "\n";
    }
    return 0;
}