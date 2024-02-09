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

#include "SortTester.cpp" // Default included SortTester.h instead, which caused an error when using VSCode but not in ZyBooks

using namespace std;

bool singleBubblePass(SortTester &tester, unsigned int size, unsigned int passNum) {
    bool sorted = true;
    bool lowToHigh = passNum % 2 == 1; // Determine sorting direction
    int newLastSwapIndex = 0;

    if (lowToHigh) {
        for (unsigned int index = 0; index < size - 1; ++index) {
            if (tester.compare(index, index + 1) > 0) {
                tester.swap(index, index + 1);
                sorted = false;
                newLastSwapIndex = index;  // Update the last swap index
            }
        }
    } else {
        for (unsigned int index = size - 1; index > 0; --index) {
            if (tester.compare(index, index - 1) < 0) {
                tester.swap(index, index - 1);
                sorted = false;
                newLastSwapIndex = index;  // Update the last swap index
            }
        }
    }

    // Check if the last element is in its correct position
    if (tester.compare(size - 1, size - 2) >= 0) {
        size = newLastSwapIndex + 1;  // Reduce the range for the next pass
    }

    return sorted;  // Return true if the pass completed without any swaps
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