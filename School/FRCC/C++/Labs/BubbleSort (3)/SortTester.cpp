//============================================================================
// Name        : Sort Testing Code
// Author      : Kenneth Horsman
// Version     : 1
// Copyright   : Your copyright notice
// Description : Basic searching examples
//============================================================================

#include <iostream>
#include <time.h>

#include "SortTester.h"

using namespace std;

SortTester::SortTester(unsigned int numEntries) {
	numCompares = 0;
	srand(time(NULL));
	for (unsigned int i=0; i < numEntries; i++ ) {
		testList.push_back( rand() % 100);
		refList.push_back( testList[i] );
	}
}

void SortTester::print(ofstream& oss) {
	for (auto & it : testList) {
		oss<<it<<" ";
	}
	oss<<"\n";
}

void SortTester::printRef(ofstream& oss) {
	for (auto & it : refList) {
		oss<<it<<" ";
	}
	oss<<"\n";
}

void SortTester::print() {
	for (auto & it : testList) {
		cout<<it<<" ";
	}
	cout<<"\n";
}

void SortTester::printRef() {
	for (auto & it : refList) {
		cout<<it<<" ";
	}
	cout<<"\n";
}

int SortTester::compare(unsigned int a, unsigned int b) {
	numCompares++;
	return testList[a] - testList[b];
}
int SortTester::compareRef(unsigned int a, unsigned int b) {
	return refList[a] - refList[b];
}

void SortTester::swap(unsigned int a, unsigned int b) {
	if ( (a > testList.size()) or (b > testList.size()) or (a<0) or (b<0) ) {
		cout<<"Invalid swap request of "<<a<<" and "<<b<<" no swap performed"<<endl;
		return;
	}
	int temp = testList[a];
	testList[a] = testList[b];
	testList[b] = temp;
	return;
}

void SortTester::swapRef(unsigned int a, unsigned int b) {
	if ( (a > refList.size()) or (b > refList.size()) or (a<0) or (b<0) ) {
		cout<<"Invalid swap request of "<<a<<" and "<<b<<" no swap performed"<<endl;
		return;
	}
	int temp = refList[a];
	refList[a] = refList[b];
	refList[b] = temp;
	return;
}

bool SortTester::isSorted(ofstream& oss) {
	bool sorted = true;
	for (unsigned int i=0; i < testList.size() - 1; i++) {
		if (testList[i] > testList[i+1] ) {
			sorted = false;
		}
	}
	if ( sorted ) {
		return true;
	} //implied else
	print(oss);
	return false;
}

bool SortTester::doesPassMatch(std::ofstream& oss) {
	bool listsMatch = true;
	for (unsigned int i=0; i< testList.size(); i++) {
		if (testList[i] != refList[i]) {
			listsMatch = false;
		}
	}
	//print Passed if match
	if (listsMatch) {
		return true;
	} //implied else
	oss<<"Match Test FAILED\n";
	oss<<"Expected\n";
	printRef(oss);
	oss<<"Actual\n";
	print(oss);
	return false;
}

unsigned int SortTester::getNumCompares() {
	return numCompares;
}
