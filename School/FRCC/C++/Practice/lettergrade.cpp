// Assigning a grade letter (A, B, C, D, F) based on the numerical score a student receives.

#include <iostream>
using namespace std;

bool isConvertibleToDouble(const string& str) { 

   try {
      stod(str); 
      return true;
   } 

   catch (...) { 
      return false;
   }

}

int main() {

   string input;
   double score;
   bool checkInput = true;
   char letterGrade;

   while (checkInput) {
      cout << "Enter your score: ";
      cin >> input;

      if(isConvertibleToDouble(input) && stod(input) <= 100 && stod(input) >= 0) break; // Is there a cleaner/shorter way to check range?
      else if(!isConvertibleToDouble(input)) cout << "Error: Value entered is not a number." << endl;
      else if(stod(input) > 100 || stod(input) < 0) cout << "Error: Value entered must in range 0 - 100." << endl;
   
   }

   score = stod(input);

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