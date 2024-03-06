//============================================================================
// Name        : Kenneth Horsman
// Author      : Bonnie Bell
// Version     :
// Copyright   : Your copyright notice
// Description : Quick and Merge Sort
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>
#include <vector>

#include "SortTester.cpp"

using namespace std;

typedef unsigned int uint;


// Sorts a vector by placing all values lesser than the value at pivotIndex to its left (not necessarily sorted)
uint partition(SortTester &tester, uint start, uint end) {
   
   uint midIndex = (start + end) / 2; // Find middle index based on given range
   tester.swap(start, midIndex); // Swap the lowest element of the range with middle index for storage
   uint pivotIndex = start; // set pivotIndex to the first element

   for(uint i = start + 1; i <= end; i++) { // For each value in the vector except the first element... [note: this is a bubble sort]
      if (tester.compare(i, start) < 0) { // if the value at i is less than the first element (middle value)...
         tester.swap(i, ++pivotIndex); // swap the value at that index with pivotIndex, which has been incremented
         
      } /* End of if statement that checks if i is less than start */
      
   }/* End of for loop that runs through each value of the vector */

   tester.swap(start, pivotIndex); // Places pivotIndex's value in the correct location within the vector by swapping it with the mid value that we stored
   return pivotIndex; // return the pivotIndex (where the midIndex element was placed)
   
} /* end of partition function */


void quickSort(SortTester &tester, uint start, uint end) {

   if (start < end) { // In each recursion, check that the range is still greater than 1
      uint pivotIndex = partition(tester, start, end); // Find pivotIndex using partition function
      
      if (pivotIndex != start){ // If pivotIndex is not equal to start... [note: this means there is still an unsorted vector to the left of the pivotIndex]
         quickSort(tester, start, pivotIndex-1); // Sort the vector between the start and pivotIndex - 1
         
      } /* End of if state that checks if the element of pivotIndex is NOT 0 */
      
      quickSort(tester, pivotIndex+1, end); // Sort the right side of the vector
      
   } /* end of if statement that checks if the range is greater than 1 */

} /* end of quickSort function */

int main() {
    uint size = 20;
    SortTester tester = SortTester(size);
    cout<<"Unsorted"<<endl;
    tester.print();
    quickSort(tester, 0, size-1);
    if (tester.isSorted()) {
        cout<<"PASSED List Sorted (5 pts)"<<endl;
    }
    else {
        tester.print();
        cout<<"FAILED List not Sorted"<<endl;
    }

}
