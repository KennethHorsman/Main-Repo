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

#include "SortTester.h"

using namespace std;

bool singleBubblePass(SortTester &tester, unsigned int size, unsigned int passNum) {
	bool sorted = true;
// Insert your code here 
//
//
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
