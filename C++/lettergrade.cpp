// Assigning a grade letter (A, B, C, D, F) based on the numerical score a student receives.

#include <iostream>
using namespace std;

int main() {

   int score;
   char letterGrade;

   cout << "Enter your score: ";
   cin >> score;

   if (score >= 90 && score <= 100) { 
      letterGrade = 'A'; 
   } else if (score >= 80 && score < 90) {
      letterGrade = 'B'; 
   } else if (score >= 70 && score < 80) {
      letterGrade = 'C'; 
   } else if (score >= 60 && score < 70) {
      letterGrade = 'D'; 
   } else {
      letterGrade = 'F'; 
   }
  
   cout << "Your grade is: " << letterGrade << endl;

   return 0;
}