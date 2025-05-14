uint partition(SortTester &tester, uint start, uint end) {
   
   uint midIndex = (start + end) / 2; // Find middle index based on given range
   tester.swap(start, midIndex); // Swap the low end of the range with middle index
   uint pivotIndex = start; // set pivotIndex to the midIndex

   // loop from start+1 to end (inclusive)
   for(uint i = start + 1; i <= end; i++) { // For each value in the (now high) part of the vector except midIndex...
      if (tester.compare(i, start) < 0) { // if the value at i is less than the low end value...
         tester.swap(i, ++pivotIndex); // swap the value at that index with pivotIndex, THEN increment pivotIndex
         
      } /* End of if statement that checks if i is less than start */
      
   }/* End of for loop that runs through each value of the vector */

   tester.swap(start, pivotIndex); // Swap the low end value with pivotIndex so all values less than the value of midIndex are to the left of it
   return pivotIndex; // return the pivotIndex, which is where the midIndex element was placed
   
} /* end of partition function */


void quickSort(SortTester &tester, uint start, uint end) {

   if (start < end) { // In each recursion, check that the range is still greater than 1
      uint pivotIndex = partition(tester, start, end); // Find pivotIndex using partition function
      
      if (pivotIndex != 0){ // If pivotIndex is not the first element...
         quickSort(tester, start, pivotIndex-1); // Sort the vector between the start and pivotIndex - 1
         
      } /* End of if state that checks if the element of pivotIndex is NOT 0 */
      
      else { // If it is...
         quickSort(tester, pivotIndex+1, end); // sort the vector between pivotIndex + 1 and the end
         
      } /* End of if statement that executes if pivotIndex is 0 */
      
   } /* end of if statement that checks if the range is greater than 1 */

} /* end of quickSort function */