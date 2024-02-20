// Author: Kenneth Horsman
// Description: Creates fan objects and displays custom details

#include "Fan.h"

int main() {
    Fan fan1; 
    fan1.setSpeed(FAST); 
    fan1.setRadius(10.0); 
    fan1.setColor("yellow"); 
    fan1.setState(true); 

    Fan fan2; 
    fan2.setSpeed(MEDIUM); 
    fan2.setRadius(5.0);
    fan2.setColor("blue"); 
    fan2.setState(false); 

    fan1.displayFan(); 
    fan2.displayFan(); 

    return 0;
} // End of main function
