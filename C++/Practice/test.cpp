
#include <iostream>
#include <vector>
using namespace std;

void PrintSize(vector<int> numsList) {
   cout << "size " << numsList.size() << endl;   
}

int main() {
   int currVal;
   vector<int> intList(4);

   PrintSize(intList); 
   
   cin >> currVal;
   while (currVal >= 0) {
      intList.push_back(currVal);
      cin >> currVal;
   }

   PrintSize(intList);

   intList.clear();

   PrintSize(intList);

   return 0;
}