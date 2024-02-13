/*
 * Record Class
 *
 *  Created on: Jan 25, 2021
 *      Author: cj6bo
 */

#include <iostream>

class Record
{
    private:
		std::string firstName;
		std::string lastName;
		int yearsInService;
		int incomeGrade;
		int reviewPerformance;

    public:
		enum fieldType{
			firstNameField,
			lastNameField,
			yearsInServiceField,
			incomeGradeField,
			reviewPerformanceField
		};
        Record(std::string firstName, std::string lastName, int start, int grade , int review);
        void print();

        // compares specified field between two Records
        // returns 0 if equal,
        // returns <0 if compared object is lesser,
        // returns >0 if compared object greater
        int compare(fieldType field, Record* compareRecord);
};
