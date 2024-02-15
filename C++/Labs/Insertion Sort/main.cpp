
//============================================================================
// Name        :
// Author      : Kenneth Horsman
// Version     :
// Copyright   : Your copyright notice
// Description : Binary Insertion Sort
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>

#include "SortTester.cpp"

using namespace std;

typedef unsigned int uint;

// Function to find the insertion location for the next element using binary search
uint findInsertionLocation(SortTester &tester, uint low, uint high, uint key) {
    // Binary search loop to find insertion location
    while (low <= high) { // While there is a range to search in..
        uint mid = (low + high) / 2; // Find the middle of the range

        if (tester.compare(mid, key) <= 0) // If the key is greater than the middle..
            low = mid + 1; // Remove the left half of the range + the current middle element
        else
            high = mid - 1; // Else, remove the right half of the range + the current middle element

        if (mid == low) // When the search comes down to a single element..
            break; // Exit while loop
    }

    return low; // Return insertion location (mid is equal to low but out of scope)
}

// Function to perform binary insertion sort
void insertionSort(SortTester &tester, uint size) {
    for (uint index = 1; index < size; ++index) { // Assume the first element is sorted and loop through each other element
        uint currentIndex = index; // Store current index in order to leave it untouched for the while loop below

        uint pos = findInsertionLocation(tester, 0, currentIndex - 1, currentIndex); // Find the insertion location for the curr element


        while (currentIndex > pos) { // While the index of the curr element is greater than its insertion location..
            tester.swap(currentIndex, currentIndex - 1); // Swap current element with the previous one
            --currentIndex; // Decrement index to test the next left-adjacent element
        }
    }
}

int main() {
	uint size = 10;
	SortTester tester = SortTester(size);
	cout<<"Unsorted"<<endl;
	tester.print();
	insertionSort(tester, size);
	if (tester.isSorted()) {
		cout<<"PASSED List Sorted (10 pts)"<<endl;
	}
	else {
		tester.print();
		cout<<"FAILED List not Sorted"<<endl;
	}

	if (tester.areComparesBinary()) {
		cout<<"PASSED Binary Insertion Sort (15 pts)"<<endl;
	}
	else {
		cout<<"FAILED Binary Insertion Sort"<<endl;
	}

	if (tester.isSortStable()) {
		cout<<"PASSED Extra Credit - sort is stable (5pts)"<<endl;
	}
	else {
		cout<<"Sort is not stable - swap occured among entries with same value"<<endl;
	}
}
