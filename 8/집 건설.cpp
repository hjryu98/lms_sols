#include <iostream>
#include <algorithm>
using namespace std;
int t, n, arr[1005];
int main() {
    cin >> t;
    while (t--) {
        int ans = 0;
        cin >> n;
        for (int i = 0; i < n; i++) cin >> arr[i];
        sort(arr, arr + n);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dist = arr[j] - arr[i];
                int s = j + 1;
                int e = n - 1;
                while (s <= e) {
                    int mid = (s + e) / 2;

                    if (arr[mid] - arr[j] == dist) {
                        ans++;
                        break;
                    }
                    if (arr[mid] - arr[j] < dist) s = mid + 1;
                    else e = mid - 1;
                }
            }
        }
        cout << ans << "\n";
    }

    return 0;
}