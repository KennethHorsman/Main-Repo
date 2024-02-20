#include "Fan.h"
#include <iostream>

using namespace std;

SLOW = 1;
MEDIUM = 2;
FAST = 3;

id = 0;

Fan::Fan() {
    speed = SLOW;
    isOn = false;
    radius = 5.0;
    color = "blue";
    id++; // Increments id for each fan created
} // End of constructor


void Fan::setSpeed(int newSpeed) {
    speed = newSpeed;
} // End of speed mutator
int Fan::getSpeed() const {
    return speed;
} // End of speed accessor


void Fan::setState(bool state) {
    isOn = state;
} // End of state mutator
bool Fan::getState() const {
    return isOn;
} // End of state accessor


void Fan::setRadius(double newRadius) {
    radius = newRadius;
} // End of radius mutator
double Fan::getRadius() const {
    return radius;
} // End of radius accessor


void Fan::setColor(string &newColor) {
    color = newColor;
} // End of color mutator
string Fan::getColor() const {
    return color;
} // End of color accessor


void Fan::displayFan() const {
    cout << "Fan ID: " << id << ", ";
    if (isOn) {
        cout << "Speed: " << speed << ", Color: " << color << ", Radius: " << radius << std::endl;
    } // End of output statement if fan is on
    else {
        cout << "Color: " << color << ", Radius: " << radius << ", Fan is off" << std::endl;
    } // End of output statement if fan is off
} // End of displayFan method