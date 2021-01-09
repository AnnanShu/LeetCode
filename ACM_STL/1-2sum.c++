#include <vector>  
#include <iostream>
#include<algorithm>
using namespace std; 
// vector<int> twoSum(vector<int>& nums, int target) {
//     vector<int> ans;
//     vector<int> temp;
//     temp=nums;
//     int n=temp.size();
//     sort(temp.begin(),temp.end());
//     int i=0,j=n-1;
//     while(i<j){  
//         if(temp[i]+temp[j]>target)j--;
//         else if(temp[i]+temp[j]<target)i++;
//         else break; 
//     }
//     if(i<j){
//     for(int k=0;k<n;k++){
//         if(i<n&&nums[k]==temp[i]){
//             ans.push_back(k);
//             i=n;
//         }
//         else if(j<n&&nums[k]==temp[j]){
//             ans.push_back(k);
//             j=n;
//         }
//         if(i==n&&j==n)return ans;
//     }
//     }
//     return ans;
// }

int main(){
	int i;
	cin >> i;
    for (int j=1; j<=i;j++){
        cout << j << endl;
    }
	// cout << i << endl;
	return 0;
}


// 作者：yun-yu-chen
// 链接：https://leetcode-cn.com/problems/two-sum/solution/san-chong-fang-fa-bao-li-shuang-zhi-zhen-ha-xi-san/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。