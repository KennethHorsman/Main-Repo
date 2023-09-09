// A program that determines if a student has passed or failed based on their grade.

#include <iostream>
using namespace std;

int main() {

   int score;
   bool passed;

   cout << "Enter your score: ";
   cin >> score;

   passed = (score >= 50) ? true : false;
   
   if (passed) {
      cout << "You passed!" << endl;
   } else {
      cout << "You failed!" << endl;
   }

   return 0;
}