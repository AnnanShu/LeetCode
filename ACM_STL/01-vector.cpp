#include<string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// cstdlib 
// qsort(), rand(), malloc()

// ctime
// time(0)  from 1970 to now second number
// clock   ms
// #include<ctime>
// int a = clock();
// clock() - a;

// vector is actually a template, so we need to initial the type 
vector<int> arr1(100);
vector<int> list;
int main(){
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);
    list.push_back(4);
    list.push_back(5);

    list.empty();
    // clear the list O(n)
    // list.clear();

    // traverse the whole list
    for(int i = 0; i < list.size(); i++)
        cout << "the " << i << "-th element in the list is: " << list[i] << endl;
    
    //Iterator
    vector<int>::iterator it;
    for(it = list.begin(); it != list.end(); it++){
        cout << *it << endl;
    }

    // String
    string str1 = "Hello world";
    str1.push_back('!');
    cout << str1 << endl; // Hello world!

    int arr[] = {1, 2, 4, 6, 3, 0};
    sort(arr, arr + 6);
    for(auto num: arr){
        cout << num << "\t";
    }


    return 0;
}