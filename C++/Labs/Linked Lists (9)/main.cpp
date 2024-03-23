
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
    // Initialize carry as a static variable
    static int carry = 0; // 

    // Base case: If both lists are nullptr and there is no carry, return 0
    if (listA == nullptr && listB == nullptr && carry == 0) {
        // Reset carry after computation
        // carry = 0;
        return 0;
    }

    // Initialize sum as the sum of the digits in the current nodes and the carry
    int sum = carry;
    if (listA != nullptr)
        sum += listA->data;
    if (listB != nullptr)
        sum += listB->data;

    // Calculate carry
    carry = sum / 10;
    sum %= 10;

    // Return the sum modulo 10 to get the current digit of the result
    return sum + addLists(listA != nullptr ? listA->next : nullptr, listB != nullptr ? listB->next : nullptr) * 10;
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