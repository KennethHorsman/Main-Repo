#include "Record.h"

using namespace std;

Record::Record(std::string first, std::string last, int years, int grade , int review) {
	firstName = first;
	lastName = last;
	yearsInService = years;
	incomeGrade = grade;
	reviewPerformance = min(3,review);

}
void Record::print() {
	cout<<"Name: "<<lastName<<", "<<firstName<<", years in service:"<<yearsInService
			<<", grade: "<<incomeGrade<<", last review: ";
	switch (reviewPerformance) {
	case 0: cout<<"Improvement Plan"<<endl; break;
	case 1: cout<<"Below Expectations"<<endl; break;
	case 2: cout<<"Meets Expectations"<<endl; break;
	case 3: cout<<"Outstanding"<<endl; break;
	}
}

// compares specified field between two Records
// returns 0 if equal,
// returns <0 if compared object is lesser,
// returns >0 if compared object greater
int Record::compare(Record::fieldType field, Record* compareRecord) {
	return 0;
}
