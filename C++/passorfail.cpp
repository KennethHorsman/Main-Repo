// A program that determines if a student has passed or failed based on their grade.

#include <iostream>
using namespace std;

int main() {

   int score;
   bool passed;

   cout << "Enter your score: ";
   cin >> score;

   passed = (score >= 60) ? true : false;
   
   cout << (passed ? "You passed!" : "You failed!") << endl;

   return 0;
}