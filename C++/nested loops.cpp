#include <iostream>
using namespace std;

int main() {
   int initialValue;
	int finalValue;
   int i;
   int j;

   cin >> initialValue;
	cin >> finalValue;
   
   for (i = initialValue; i <= finalValue; ++i) {
      for (j = 0; j < i; ++j) {
         cout << "%";
      }
      cout << endl;
   }
         
      

   return 0;
}