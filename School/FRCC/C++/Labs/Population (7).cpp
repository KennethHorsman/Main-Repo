//============================================================================
// Name        : Kenneth Horsman
// Author      : Bonnie Bell
// Version     :
// Copyright   : Your copyright notice
// Description : Population Modeling Problem
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>

using namespace std;

typedef unsigned int uint;

uint updatePopulation(uint currentPopulation) {
	uint numBirths = .0185*(currentPopulation);
	uint numDeaths = .0008*(currentPopulation);
	return currentPopulation + numBirths - numDeaths;
}

uint howManyGenerations(uint startAmount, uint finalAmount) {
    if (startAmount >= finalAmount) { // If curr pop is larger than or equal to the final pop...
        return 0; // exit the loop by returning 0 with no recursion
    } /* end of if statement to exit the recursion loop */
	else {
        uint nextAmount = updatePopulation(startAmount); // Get the pop of the next generation 
        return 1 + howManyGenerations(nextAmount, finalAmount); // Recursion with next gen's population 
																// Return "1 + FUNCTION" so the final return sums the num of calls
    } /* end of curr recursive call */
}


int main() {

	uint finalAmount = 1000000;
	uint startAmount = 100;
	if (howManyGenerations(startAmount, finalAmount) == 537) {
		cout<<"PASSED start=100, final=1000000"<<endl;
	}
	return 0;
}
