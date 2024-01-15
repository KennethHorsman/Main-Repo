#include <iostream>
#include <stdexcept>
using namespace std;


int main() {
   int value = 2;
   try {
      if(value == 1)
        throw 2;                 
      else if(value == 2)
        throw '2';                
      else if(value == 3)
        throw 2.0;                
   }
   catch(int a) {
      cout << "\n Variable type 1 exception caught.";
   }
   catch(char ch) {
      cout << "\nVariable type 2 exception caught.";
   }
   catch(double d) {
   cout << "\nVariable type 3 exception caught.";
   }
   cout << "\nEnd of program.";
}