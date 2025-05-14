
//============================================================================
// Name        : Kenneth Horsman
// Author      : Bonnie Bell
// Version     :
// Copyright   : Your copyright notice
// Description : Stacks and Queues
//============================================================================

#include <fstream>
#include <iostream>
#include <time.h>
#include <stack>
#include <queue>

using namespace std;
int evalPostfix(queue<char> expression) {
    stack<int> operands; // Stack that stores operands

    while (!expression.empty()) { // While the expression still has charaters left to iterate through...
        char current = expression.front(); // Store the current character (the front of the queue)
        expression.pop(); // Move to the next char for future operation

        if (isdigit(current)) { // If the current character is a digit...
            operands.push(current - '0'); // Get the integer value of the char and push to operands stack
        } 
        else if (current == '+' || current == '-' || current == '*' || current == '/') { // If the current char is an operator...
            if (operands.size() < 2) { // First check if there are not enough operands to perform the operation...
                cout << "Invalid postfix expression." << endl;
                return 0; 
            }
            int operand2 = operands.top(); // Get the first operand
            operands.pop(); // Move to the next char
            int operand1 = operands.top(); // Get the second operand
            operands.pop(); // Empty operands stack

        switch (current) { // Perform operation based on current char (being the operator)
            case '+':
                operands.push(operand1 + operand2); // Add operands and push result onto stack
                break;
            case '-':
                operands.push(operand1 - operand2); // Subtract operands and push result onto stack
                break;
            case '*':
                operands.push(operand1 * operand2); // Multiply operands and push result onto stack
                break;
            case '/':
                if (operand2 == 0) { // First check for division by zero
                    cout << "Division by zero error." << endl;
                    return 0;
                }
                operands.push(operand1 / operand2); // Divide operands and push result onto stack
                break; 
            } /* End of switch */
        } /* End of else if */
        else { // If the current char is not a digit or an operator...
            cout << "Invalid character in postfix expression." << endl; 
            return 0;
        } /* End of else */
    } /* End of while */

    
    if (operands.size() != 1) { // After evaluating the expression, the only element in operands should be the result
        cout << "Invalid postfix expression." << endl;
        return 0;
    }

    return operands.top(); // Return final result
}


int main() {
	std::queue<char> queue1, queue2;
	//basic simple addition
	queue1.push('1');
	queue1.push('2');
	queue1.push('+');
	cout<<"Queue1 evaluates to "<<evalPostfix(queue1)<<std::endl;
	queue2.push('5');
	queue2.push('6');
	queue2.push('7');
	queue2.push('+');
	queue2.push('1');
	queue2.push('2');
	queue2.push('+');
	queue2.push('-');
	queue2.push('*');
	queue2.push('4');
	queue2.push('/');
	cout<<"Queue2 evaluates to "<<evalPostfix(queue2)<<std::endl;
	return 0;
}

