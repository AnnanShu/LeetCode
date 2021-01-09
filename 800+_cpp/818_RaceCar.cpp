#include<vector>
#include<unordered_set>
#include<queue>
#include<math.h>
using namespace std;

class Solution{
public:
    int racecar(int target){
        m = vector<int>(target+1, 0);
        return dp(target); 
    }
private:
    vector<int> m;
    int dp(int t){
        if(m[t] > 0) return m[t];
        int n = ceil(log2(t + 1));
        // AAA...AAA(nA) best case
        if (1 << n == t + 1) return m[t] = n;

        // AA...R(n-1A + 1R) + dp(left)
        m[t] = n + 1 + dp((1 << n) - t -1);

        for(int i = 0; i < n -1; ++i){
            int cur = (1 << (n-1)) - (1 << i);
            m[t] = min(m[t], n + i + 1 + dp(t-cur));
        }
        return m[t];
    }
};
// class Solution{
// public:
//     int racecar(int target){
//         queue<pair<int, int>> q;
//         q.push({0, 1});
//         unordered_set<string> v;
//         v.insert("0_1");
//         v.insert("0_-1");

//         int steps = 0;
//         while(!q.empty()){
//             int size = q.size();
//             while(size --){
//                 auto p = q.front(); q.pop();
//                 int pos = p.first;
//                 int speed = p.second;
//                 {
//                     int pos1 = pos + speed;
//                     int speed1 = speed * 2;
//                     pair<int, int> p1{pos1, speed1}
//                 }
//             }
//         }

//     }
// };