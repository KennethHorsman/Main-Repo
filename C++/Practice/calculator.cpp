// A calculator program that takes an operator (+, -, *, /) as input to perform a specified arithmetic operation.

#include <iostream> // allows use of cout & cin
using namespace std; // prevents using std:: in front of things like cout

bool isConvertibleToDouble(const string& str) { // passes object (str) by reference as a constant string (const string&)

   try {
      stod(str); // returns true if string-to-double conversion is possible
      return true;
   } 

   catch (...) { // returns false if string-to-double conversion results in any exceptions
      return false;
   }

}

int main() { // C++ apparently requires main() to be int so it cannot be void and bypass returning 0

   string string1, string2, string3; // strings used for user input to bypass errors if they enter something invalid
   double value1, value2, result; // value 1 & 2 replace string 1 & 2 after they pass validation
   char operation; // single char used in switch statement
   bool checkInput =  true; // simply created a flag as the argument for a while loop that checks the validity of input

   while (checkInput) { // while flag is true...
      cout << "Enter first value: "; // no endl because I want the input to be taken on the same line for aesthetic purposes
      cin >> string1; // turns user input intro string1 - also, it seems like there's a hidden automatic endl after taking input

      if (isConvertibleToDouble(string1)) break; // IF the above function returns true with string1 as str, break the while loop
      else cout << "Error: Value entered is not a number." << endl; // ELSE state an error message and continue the loop
   }

   while (checkInput) {
      cout << "Enter operation (+ - * /): ";
      cin >> string3;

      if (string3 == "+" || string3 == "-" || string3 == "*" || string3 == "/") break; // why doesn't " (string3 == '+' || '-' || '*' || '/') " work?
      else cout << "Error: Operation invalid." << endl;  
   }

   while (checkInput) {
      cout << "Enter second value: ";
      cin >> string2;

      if (isConvertibleToDouble(string2) && stod(string2) != 0) break; // ensures that the user does not attempt to divide by 0
      else if (!isConvertibleToDouble(string2)) cout << "Error: Value entered is not a number." << endl; // displays accurate error messages
      else if (stod(string2) == 0) cout << "Error: Cannot divide by zero." << endl;
   }

   value1 = stod(string1); // assigns double 'value1' as 'string1' converted to a double (could technically do string1 = stod(string1) ?)
   value2 = stod(string2);
   operation = string3[0]; // cannot convert an entire string to a char variable, so it must access a specific index

   switch(operation) { // checks which case argument below is equal to the value of 'operation' and proceeds accordingly

      case('+'):
         result = value1 + value2; // this variable isn't necessary, but allows various things to be done with the result of the operation if wanted
         cout << value1 << " + " << value2 << " = " << result << endl; // outputs the operation and the result
         break; // breaks out of the switch statement instead of falling through to the next set of instructions
         
      case('-'):
         result = value1 - value2;
         cout << value1 << " - " << value2 << " = " << result << endl;
         break;

      case('*'):
         result = value1 * value2;
         cout << value1 << " * " << value2 << " = " << result << endl;
         break;

      case('/'):
         result = value1 / value2;
         cout << value1 << " / " << value2 << " = " << result << endl;
         break;

   }

   return 0; // int main() must return an int value, and 0 indicates to the OS that the program executed successfully?

}