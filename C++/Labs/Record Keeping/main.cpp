/*
 * Week 2 comparisons
 *
 *  Created on: Jan 25, 2021
 *      Author: cj6bo
 */

#include <iostream>
#include <vector>
#include "Record.h"

using namespace std;

void printRecords(vector<Record*> employees) {
	for ( auto it:employees) {
		it->print();
	}
}

void sortBy(Record::fieldType sortField, vector<Record*> &employees) {
	bool sorted = false;
	while (!sorted) {
		sorted = true;
		for (unsigned int i=0; i < employees.size()-1; i++) {
			if (employees[i]->compare(sortField, employees[i+1]) > 0 ) {
				Record* temp = employees[i];
				employees[i] = employees[i+1];
				employees[i+1] = temp;
				sorted = false;
			}
		}
 	}
}
int main() {
	std::vector<Record*> employees;
	employees.push_back(new Record("David", "Bowie", 5,  8,  0));
	employees.push_back(new Record("Kim",   "Kardashian", 15, 9, 2));
	employees.push_back(new Record("Khloe", "Kardashian", 5, 10, 3));
	employees.push_back(new Record("David", "Lee Roth", 9, 4, 1));
	employees.push_back(new Record("Greta", "Garbo", 1, 3, 5));
	cout<<"Unsorted"<<endl;
	printRecords(employees);
	cout<<"enter a field (0-4) to sort by:";
	int sortField;
	cin>>sortField;
	switch (sortField) {
	case 0: sortBy(Record::firstNameField, employees); break;
	case 1: sortBy(Record::lastNameField, employees); break;
	case 2: sortBy(Record::yearsInServiceField, employees); break;
	case 3: sortBy(Record::incomeGradeField, employees); break;
	case 4: sortBy(Record::reviewPerformanceField, employees); break;
	default:cout<<"Unknown field"<<endl;
	}
	cout<<endl;
	cout<<"Sorted"<<endl;
	printRecords(employees);
	return (0);
}

