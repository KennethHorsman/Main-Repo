
#include <iostream>
#include <vector>
using namespace std;

class Greet {
   public:
   Greet();
};

Greet::Greet() {
   cout << "Hello";
}

int main() {
   Greet greeting;
   return 0;
}