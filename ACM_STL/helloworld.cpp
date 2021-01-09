#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std;

int main(){
    cout << "hello world!" << endl;
    string line;
    // read a whole line
    getline(cin, line);
    cout << "this line is: " << line;
    return 0;
}