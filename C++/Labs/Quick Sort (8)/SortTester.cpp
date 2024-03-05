
//============================================================================
// Name        : Sort Testing code
// Author      : Bonnie Bell
// Version     :
// Copyright   : Your copyright notice
// Description : Basic searching examples
//============================================================================

#include <iostream>
#include <time.h>
#include <cmath>

#include "SortTester.h"

using namespace std;

SortTester::SortTester(unsigned int numEntries) {
	numCompares = 0;
	stableSort = true;
	srand(time(NULL));
	for (unsigned int i=0; i < numEntries; i++ ) {
		testList.push_back( rand() % 100);
	}
}

void SortTester::print() {
	for (auto & it : testList) {
		cout<<it<<" ";
	}
	cout<<"\n";
}

int SortTester::compare(unsigned int a, unsigned int b) {
	numCompares++;
	return testList[a] - testList[b];
}

void SortTester::swap(unsigned int a, unsigned int b) {
	if ((testList[a] == testList[b]) and (a != b)) {
		stableSort= false;
	}
	if ( (a > testList.size()) or (b > testList.size()) ) {
		cout<<"Invalid swap request of "<<a<<" and "<<b<<" no swap performed"<<endl;
		return;
	}
	int temp = testList[a];
	testList[a] = testList[b];
	testList[b] = temp;
	return;
}

bool SortTester::isSorted() {
	bool sorted = true;
	for (unsigned int i=0; i < testList.size() - 1; i++) {
		if (testList[i] > testList[i+1] ) {
			sorted = false;
		}
	}
	if ( sorted ) {
		return true;
	} //implied else
	print();
	return false;
}

bool SortTester::areComparesBinary() {
	unsigned int n = testList.size();
	return numCompares < 2*n*log2(n);
}
bool SortTester::isSortStable() {
	return stableSort;
}
