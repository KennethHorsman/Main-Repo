//============================================================================
// Name        : Bubble Sort (Main)
// Author      : Kenneth Horsman
// Version     : 1
// Copyright   : Your copyright notice
// Description : Basic searching examples
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>

#include "SortTester.cpp" // Default included SortTester.h instead, which caused an error

using namespace std;

/*  function bubbleSort(array)
    n = length of array
    sorted = false
    lowToHigh = true  // Flag to indicate whether to sort from low to high or high to low

    while not sorted
        sorted = true
        newLastSwapIndex = 0

        if lowToHigh
            for i from 1 to n-1  // Sort from low to high
                if array[i] < array[i-1]
                    swap array[i] and array[i-1]
                    sorted = false
                    newLastSwapIndex = i  // Update the last swap index

        else
            for i from n-1 to 1  // Sort from high to low
                if array[i] < array[i-1]
                    swap array[i] and array[i-1]
                    sorted = false
                    newLastSwapIndex = i  // Update the last swap index

        // If no swaps were made, the array is already sorted
        if sorted
            break

        n = newLastSwapIndex  // Reduce the range for the next pass
        lowToHigh = not lowToHigh  // Toggle the sorting direction for the next pass */


bool singleBubblePass(SortTester &tester, unsigned int size, unsigned int passNum) {
	bool sorted = false, lowToHigh = true;

	while (!sorted) {
		sorted = true;
		int lastSwapIndex = 0;

		if (lowToHigh) {
			for (int index = 0; index < size - 1; ++index) {
				if (tester[index] < )
			}
		}

	}


	return sorted;
}

int main() {
	unsigned int size = 10;
	SortTester tester = SortTester(size);
	cout<<"Unsorted"<<endl;
	tester.print();
	bool sorted = false;
	unsigned int numPasses = 0;
	while (not sorted) {
		sorted = true;
		numPasses++;
		sorted = singleBubblePass(tester, size, numPasses); //this is the function you are defining
   }
   tester.print();
}