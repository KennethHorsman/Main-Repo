// A program that determines if a student has passed or failed based on their grade.

#include <iostream>
using namespace std;

int main() {

   int score;
   bool passed;
   bool validInput = false;

   while (!validInput) {

      cout << "Enter your score: ";
      cin >> score;

      validInput = (score >= 0 && score <= 100) ? true : false;
      
      if (!validInput) {
         cout << "ERROR: Score must be between 0 and 100." << endl;
      }

   }

   passed = (score >= 60) ? true : false;
   
   cout << (passed ? "You passed!" : "You failed!") << endl;

   return 0;
}