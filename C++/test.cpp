// Assigning a grade letter (A, B, C, D, F) based on the numerical score a student receives.

#include <iostream>
using namespace std;

int main() {

   int score;
   int scoreDivided;
   bool passed = false;

   cout << "Enter your score: \n";
   cin >> score;

   scoreDivided = score / 50;

   switch(scoreDivided) {

      case(1):
      case(2):
         passed = true;
         break;

      default:
         break;
   
   if (passed) {
      cout << "You passed!\n";
   }
   else {
      cout << "You failed!\n";
   }
   }

   return 0;
}