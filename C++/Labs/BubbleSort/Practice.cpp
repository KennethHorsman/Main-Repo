/*
Team Members: Kenneth Horsman, Aaron Villalobos
Description: Bubble Sort Practice
*/

#include <iostream>
using namespace std;

void BubbleSort(int numbers[], int numbersSize) {
    int temp;

    for (int i=0; i<numbersSize-1; ++i) {
        for (int index = 0; index < numbersSize -1; ++index) {
            if (numbers[index] > numbers[index+1]) { // If curr index's value more than the next...
                temp = numbers[index]; // Store curr index's value in temp
                numbers[index] = numbers[index + 1]; //
                numbers[index + 1] = temp;
            }
        }
    }

    return;
}


int main() {

int numbers[] = {1,4,6,2,9};
int numbersSize = 5;

cout << "Original Array: ";
for (int index = 0;  index < numbersSize; ++index) {
    cout << numbers[index] << " ";
}
cout << endl;

BubbleSort(numbers, numbersSize);

cout << "Sorted Array: ";
for (int index = 0;  index < numbersSize; ++index) {
    cout << numbers[index] << " ";
}
cout << endl;

return 0;

}