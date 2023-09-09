// A calculator program that takes an operator (+, -, *, /) as input to perform a specified arithmetic operation.

#include <iostream>
using namespace std;

int main() {

   double value1;
   double value2;
   double result;
   char operation;

   cout << "Enter first value: ";
   cin >> value1;

   cout << "Enter operation (+ - * /): ";
   cin >> operation;

   cout << "Enter second value: ";
   cin >> value2;

   switch(operation) {

      case('+'):
         result = value1 + value2;
         cout << value1 << " + " << value2 << " = " << result << endl;
         break;
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
      default:
         cout << "ERROR: Invalid operation." << endl;
         break;
         
   }

   return 0;
}