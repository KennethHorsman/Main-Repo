#include <iostream>
using namespace std;

int main() {
    int sum, val;
    
    cin >> val;
    sum = 0;
    
    while (val != -1) {
        sum += val;
        cin >> val;
    }
    cout << sum;
}