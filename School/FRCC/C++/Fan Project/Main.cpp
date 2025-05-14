// Author: Kenneth Horsman
// Description: Creates fan objects and displays custom details

#include "Fan.cpp"

int main() {
    Fan fan1; // Could do Fan *fan1 = new Fan;
    fan1.setSpeed(Fan::FAST); 
    fan1.setRadius(10.0); 
    fan1.setColor("Yellow"); 
    fan1.setState(true); 

    Fan fan2; 
    fan2.setSpeed(Fan::MEDIUM); 
    fan2.setRadius(5.0);
    fan2.setColor("Blue"); 
    fan2.setState(false); 

    fan1.displayFan(); 
    fan2.displayFan(); 

    return 0;
} // End of main function
