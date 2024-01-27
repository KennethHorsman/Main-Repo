// Kenneth Horsman
/* Given a sorted array of n integers nums[] = [1, 3, 5, 7, 19] and a target values of 7 & 11, 
determine if the target exists in the array in logarithmic time using the binary search algorithm. 
If target exists in the array, print the index of it. If the target does not exist print Element not found.

Create a function called binarySearch that accepts three arguments and returns an integer value of the index.
Input: nums[] = [1, 3, 5, 7, 19] target = 7
Output: Element found at index 3 */

#include <iostream>
#include <vector> // required for vector<int> numbers
#include <algorithm> // required for cin.ignore(numeric_limits<streamsize>::max(), '\n');
using namespace std;

int BinarySearch(int numbers[], int target, int numbersSize) { // Not sure if you meant 3 args as in two targets or this
    int leftSide = 0, rightSide = numbersSize -1; // establishes first and last index of search
    
    while (leftSide <= rightSide) { // if the value is not present, leftSide will become greater than rightSide via the calculation below
        int middle = (leftSide + rightSide) / 2; // establishes middle index based on first and last index
        if (numbers[middle] == target) { // if the value at index middle is the target value...
            return middle; // return the index middle
        }
        else if (numbers[middle] < target) { // if the target is greater than the current value...
            leftSide = middle + 1; // discard the left side of the search and the current middle index
        }
        else { // only other option: if the target is less than the current value...
            rightSide = middle - 1; // discard the right side of the search and the current middle index
        }   
    }
    
    return -1; // -1 used as a return value to indicate that the target value was not present
}

int main() {
    int numbers[] = {1,3,5,7,19}; // Since the values and size are pre-defined, use an array (which is better for performance than a vector)
    int numbersSize = 5, target, targetIndex;
    bool targetGiven = false;
    
    while (!targetGiven) { // used pre-set bool as a flag to indicate whether the user has submit a valid target value
        cin >> target;
        if (cin.fail()) { // Since the variable is an int, cin will only successfully accept an int
            cin.clear(); // Clears the error flag to allow future cin operations
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); /* Ignores the maxiumum number of characters that can be read by an input stream
            and stops after it reaches the newline that is created at the end of the cin operation, allowing future cin operations */
        }
        else {
            targetGiven = true; // changing the bool exits the loop
        }
    }
    
    targetIndex = BinarySearch(numbers, target, numbersSize);
    if (targetIndex != -1) {
        cout << "Element found at index " << targetIndex;
    }
    else {
        cout << "Element not found in the array";
    }
    
    return 0;
}