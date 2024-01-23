/* Write a program to calculate the score from a throw of five dice. Scores are assigned to different categories for singles, 
three of a kind, four of a kind, five of a kind, full house, and straight. Follow each step to gradually complete all functions.

Step 1 (3 pts). Complete the CheckSingles() function. Return the sum of all values that match parameter goal. 
Update the FindHighScore() function using a loop to call CheckSingles() six times with parameters being 1 - 6. 
Return the highest score from all function calls. 
If input is: 2 4 1 5 4, the output is: High score: 8

Step 2 (3 pts). Complete the CheckThreeOfKind(), CheckFourOfKind(), and CheckFiveOfKind() functions. 
Hint: Since the values are in ascending order, same values are stored in consecutive index locations. 
Return 30 from CheckThreeOfKind() if the dice contain at least three of the same values. Ex: (2, 3, 3, 3, 6). 
Return 40 from CheckFourOfKind() if the dice contain at least four of the same values. Ex: (4, 4, 4, 4, 5). 
Return 50 from CheckFiveOfKind() if the dice contain five identical values. Ex: (5, 5, 5, 5, 5). 
Update the FindHighScore() function to call the three functions and return the highest score from all function calls. 
Submit for grading to confirm five tests pass.
If input is: 2 4 4 5 4, the output is: High score: 30

Step 3 (2 pts). Complete the CheckFullHouse() function to return 35 if the dice contain a full house (a pair and three of a kind). 
Ex: (1, 1, 3, 3, 3). Note: Five of a kind also satisfies the definition of a full house since (4, 4, 4, 4, 4) includes a pair of 4s and three 4s. 
Update the FindHighScore() function to call CheckFullHouse() and return the highest score from all function calls. 

Step 4 (2 pts). Complete the CheckStraight() function to return 45 if the dice contain a straight of (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6). 
Update the FindHighScore() function to call CheckStraight() and return the highest score from all function calls. */

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;


// Update highest count
int updatehighScore(int currentCount, int highScore) {
   if (currentCount > highScore) {
      highScore = currentCount;
   }
   return highScore;
}


// Find the highest number of times an element was repeated
int GetMostRepetitions(vector<int>& diceValues) {
   int currentCount = 0, highScore = 0;
   
   for (int valueToFind = 1; valueToFind <= 6; ++valueToFind) {
      for (int diceValuesIndex = 0; diceValuesIndex < 5; ++diceValuesIndex) {
         if (diceValues.at(diceValuesIndex) == valueToFind) {
            currentCount += 1;
         }
      }
      
      if (currentCount > highScore) {
         highScore = currentCount;
      }
      
      currentCount = 0;
   }
   
   return highScore;
}


// Add all occurences of goal value
int CheckSingles(vector<int>& diceValues, int valueToFind) {
   int sum = 0;
   
   for (int diceValuesIndex = 0; diceValuesIndex < 5; ++diceValuesIndex) {
      if (diceValues.at(diceValuesIndex) == valueToFind) {
         sum += valueToFind;
      }
   }
   return sum;
}


// Check for three of a kind (score = 30)
int CheckThreeOfKind(vector<int>& diceValues) {
   if (GetMostRepetitions(diceValues) == 3) {
      return 30;
   }
   else {
      return 0;
   }
}


// Check for four of a kind (score = 40)
int CheckFourOfKind(vector<int>& diceValues) {
   if (GetMostRepetitions(diceValues) == 4) {
      return 40;
   }
   else {
      return 0;
   }
}

// Check for five of a kind (score = 50)
int CheckFiveOfKind(vector<int>& diceValues) {
   if (GetMostRepetitions(diceValues) == 5) {
      return 50;
   }
   else {
      return 0;
   }
}

// Check for full house (score = 35)
int CheckFullHouse(vector<int>& diceValues) {
   bool twoUniqueValues = false, threeRepetitions = false;
   set<int> testSet(diceValues.begin(), diceValues.end()); // Sets can only hold unique values
   
   if (GetMostRepetitions(diceValues) == 3) {
      threeRepetitions = true;
   }
   
   if (testSet.size() == 2) {
      twoUniqueValues = true;
   }

   if (threeRepetitions && twoUniqueValues) {
      return 35;
   }
   else if (CheckFiveOfKind(diceValues) == 50) {
      return 35;
   }
   else {
      return 0;
   }

}

// Check for straight (score = 45)
int CheckStraight(vector<int>& diceValues) {
   bool sequentialNumbers = true;

   for (int diceValuesIndex = 0; diceValuesIndex < 4; ++diceValuesIndex) {
      if (diceValues.at(diceValuesIndex) != diceValues.at(diceValuesIndex + 1) - 1) {
         sequentialNumbers = false;
         break;
      }
   }

   if (sequentialNumbers) {
      return 45;
   }
   else {
      return 0;
   }
}

// Find high score
int FindHighScore(vector<int>& diceValues) {
   int currentCount, highScore; 
   highScore = 0;

   if (CheckFiveOfKind(diceValues) == 50) {
      return highScore = 50;
   }
   
   if (CheckStraight(diceValues) == 45) {
      return highScore = 45;
   }
   
   if (CheckFourOfKind(diceValues) == 40) {
      return highScore = 40;
   }
   
   if (CheckFullHouse(diceValues) == 35) {
      return highScore = 35;
   }
   
   if (CheckThreeOfKind(diceValues) == 30) {
      return highScore = 30;
   }
   
   for (int valueToFind = 1; valueToFind <= 6; ++valueToFind) {
      currentCount = CheckSingles(diceValues, valueToFind);
      highScore = updatehighScore(currentCount, highScore);
   }
   
   return highScore;
}

int main() {
   vector<int> diceValues(5);
   int highScore = 0;

   // Fill array with five values from input
   for(int diceValuesIndex = 0; diceValuesIndex < 5; ++diceValuesIndex) {
      cout << "Enter a value for die " << diceValuesIndex + 1 << ": ";
      cin >> diceValues.at(diceValuesIndex);
      if (cin.fail() || diceValues.at(diceValuesIndex) > 6) { // Since the variable is an int, cin will only accept an int
         cout << "Invalid number entered." << endl;
         cin.clear(); // Clears the error flag to allow future cin operatoins
         cin.ignore(numeric_limits<streamsize>::max(), '\n'); // This code ignores all the characters in the buffer & creates a new line
         --diceValuesIndex; 
      }
   }

   // Place values in ascending order
   sort(diceValues.begin(), diceValues.end());

   // Find high score and output
   highScore = FindHighScore(diceValues);
   cout << "High score: " << highScore << endl;

   return 0;
}
