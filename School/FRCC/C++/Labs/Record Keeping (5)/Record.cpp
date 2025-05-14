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
int compareFields(auto& field1, auto& field2) { // Calls data by reference using type auto which lets compiler determine the type
    if (field1 < field2) return -1; // returns <0 if compared object is lesser
    if (field1 > field2) return 1; // returns >0 if compared object greater
    return 0; // returns 0 if equal
}

int Record::compare(fieldType field, Record* compareRecord) {
    switch (field) { // we cannot call "field" directly because that's not an actual field name
        case firstNameField:
            return compareFields(this->firstName, compareRecord->firstName);
        case lastNameField:
            return compareFields(this->lastName, compareRecord->lastName);
        case yearsInServiceField:
            return compareFields(this->yearsInService, compareRecord->yearsInService);
        case incomeGradeField:
            return compareFields(this->incomeGrade, compareRecord->incomeGrade);
        case reviewPerformanceField:
            return compareFields(this->reviewPerformance, compareRecord->reviewPerformance);
        default:
            break; // I don't want to return 0 since that indicates the fields were the same when there was an error
    }
}



