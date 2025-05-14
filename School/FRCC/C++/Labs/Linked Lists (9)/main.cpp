
//============================================================================
// Name        : Kenneth Horsman
// Author      : Bonnie Bell
// Version     :
// Copyright   : Your copyright notice
// Description : Linked List Fun
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>

#include "Node.cpp"

using namespace std;

typedef unsigned int uint;

void printList(Node* list) {
	while (list != nullptr) {
		cout << list->data << "  ";
		list = list->next;
	}
	cout<<endl;
}

int addLists(Node* listA, Node* listB) {
    static int carry = 0; // Initialize carry as a static variable to retain its value

    if (listA == nullptr && listB == nullptr && carry == 0) { // If both lists are empty & no carry...
        return 0; // Exit function
    }

    int sum = carry; // Initialize sum with the curr value of carry

    if (listA != nullptr) // If listA is not empty...
        sum += listA->data; // Add listA's data value to sum

    if (listB != nullptr) // If listA is not empty...
        sum += listB->data; // Add listB's data value to sum

    carry = sum / 10; // Calculate carry for next operation (since data must be a single digit)
    sum %= 10; // Calculate the curr value of the result by taking the remainder of dividing sum by 10

    return sum + addLists(listA != nullptr ? listA->next : nullptr, listB != nullptr ? listB->next : nullptr) * 10;
	// Returning "sum +" ensures the resulting values after each call get added together
	// Recursively call addLists with the next nodes of listA and listB if they are not nullptr, otherwise simply pass nullptr
		// Passing nullptr instead of the node itself prevents dereferencing of nullptr
    // Multiply the recursive result by 10 to shift the digit to its correct place in the final result since the nodes are divided by 10
}


Node* genList(int number) {
	Node* headOfList = new Node(number%10);
	Node* listIterator = headOfList;
	number = number / 10;
	while (number > 0) {
		listIterator->next = new Node(number%10);
		listIterator = listIterator->next;
		number = number/10;
	}
	return headOfList;
}

int main() {
	srand(time(NULL));
	int numA = rand()%10000000;
	int numB = rand()%10000000;
	Node* listA = genList(numA);
	Node* listB = genList(numB);
	int sum = addLists(listA, listB);
	if ( sum == (numA + numB)) {
		cout<<"PASSED basic test (9 pts)"<<endl;
	}
	else {
		cout<<"FAILED expected: "<<numA + numB<<" actual: "<<sum<<endl;
	}

	int numC = rand()%100<<12;
	int numD = rand()%100;
	Node* listC = genList(numC);
	Node* listD = genList(numD);
	sum = addLists(listC, listD);
	if ( sum == (numC + numD)) {
		cout<<"PASSED A much greater than B (8 pts)"<<endl;
	}
	else {
		cout<<"FAILED expected: "<<numC + numD<<" actual: "<<sum<<endl;
	}

	int numF = rand()%100<<12;
	int numE = rand()%100;
	Node* listE = genList(numE);
	Node* listF = genList(numF);
	sum = addLists(listE, listF);
	if ( sum == (numE + numF)) {
		cout<<"PASSED B much greater than A (8 pts)"<<endl;
	}
	else {
		cout<<"FAILED expected: "<<numE + numF<<" actual: "<<sum<<endl;
	}

	return 0;
}