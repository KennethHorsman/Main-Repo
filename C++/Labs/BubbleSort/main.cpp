//============================================================================
// Name        : Bubble Sort (All hares)
// Author      : Kenneth Horsman
// Version     : 2
// Copyright   : Your copyright notice
// Description : Basic searching examples
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>

#include "SortTester.cpp"

using namespace std;

bool singleBubblePass(SortTester &tester, unsigned int lowEnd, unsigned int highEnd, unsigned int passNum) {
    bool sorted = true;
    bool lowToHigh = passNum % 2 == 1; // Determine sorting direction based on even/odd pass

    if (lowToHigh) {
        bool swapped = false; // Flag to indicate if a swap occurred in this pass
        for (unsigned int index = lowEnd; index < highEnd - 1; ++index) { // for each index in array from specified range
            if (tester.compare(index, index + 1) > 0) { // if curr value greater than the next
                tester.swap(index, index + 1); // swap them
                swapped = true; // change flag to indicate a swap occurred
            }
        }
        sorted = !swapped; // If no swap occurred, the list is sorted
    } else {
        bool swapped = false; 
        for (unsigned int index = highEnd - 1; index > lowEnd; --index) {
            if (tester.compare(index, index - 1) < 0) {
                tester.swap(index, index - 1);
                swapped = true;
            }
        }
        sorted = !swapped;
    }

    return sorted; // Return true if the pass completed without any swaps
}


int main() {
    unsigned int size = 10;
    SortTester tester = SortTester(size);
    cout << "Unsorted" << endl;
    tester.print();
    bool sorted = false;
    unsigned int numPasses = 0;
    unsigned int lowEnd = 0;
    unsigned int highEnd = size;
    while (!sorted) {
        sorted = true;
        numPasses++;
        sorted = singleBubblePass(tester, lowEnd, highEnd, numPasses); // Perform a single pass
        if (numPasses % 2 == 0) {
            highEnd--; // Remove last element on even pass
        } else {
            lowEnd++; // Remove first element on odd pass
        }
    }

    tester.print();
}