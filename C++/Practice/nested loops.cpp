#include <iostream>
using namespace std;

int main() {
   int numRows;
   int numColumns;
   int currentRow;
   int currentRowInteger;
   int currentColumn;
   char currentColumnLetter;
   
   cin >> numRows;
   cin >> numColumns;

   for (currentRow = 1, currentRowInteger = 1; currentRow <= numRows; ++currentRow, ++currentRowInteger) {
      for (currentColumn = 1, currentColumnLetter = 'A'; currentColumn <= numColumns; ++ currentColumn, ++currentColumnLetter) {
         cout << currentRowInteger << currentColumnLetter << " ";
      }
      cout << endl;
   }

   return 0;
}