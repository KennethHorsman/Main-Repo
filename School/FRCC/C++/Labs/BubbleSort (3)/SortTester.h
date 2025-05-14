/*
 * SortTester.h
 *
 *  Created on: Jan 30, 2021
 *      Author: cj6bo
 */

#include <fstream>
#include <vector>


class SortTester {
    private:
		std::vector<int> testList;
		std::vector<int> refList;
		unsigned int numCompares;

    public:
        SortTester(unsigned int numEntries);
        void swap(unsigned int a, unsigned int b);
        //returns positive number if a > b, 0 if a==b, and negative number if a < b
        int compare(unsigned int a, unsigned int b);
        void print(std::ofstream& oss);
        void print();
        unsigned int getNumCompares();
        bool isSorted(std::ofstream& oss);
        bool doesPassMatch(std::ofstream& oss);
        void runPerformanceExtraCreditTest(unsigned numPasses);
        
        ////the following functions are to be used by testbench only
        void printRef(std::ofstream& oss);
        int compareRef(unsigned int a, unsigned int b);
        void swapRef(unsigned int a, unsigned int b);
        void printRef();
};
