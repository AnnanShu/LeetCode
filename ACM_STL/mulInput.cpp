#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std;

struct node
{
    int number;
    node(int _a = 0){
        number = _a;
    }
    node* next;
};

int main(){
    int a = 3;
    float b = 5.5;
    // multiple input
    // while (cin >> a){
    //     cout << a << endl;
    // }

    node nd = node();
    nd.next = &node(4);
    node nd2 = node(2);
    cout << nd.number <<endl;
    cout << nd2.number << endl;

    // dynamic create memory
    int* number = new int;
    delete[] number;
    int* arr = new int[100];
    int* carr = (int*)malloc(100 * sizeof(int));
    printf("%d, %.3f\n", a, b);
    return 0;
}