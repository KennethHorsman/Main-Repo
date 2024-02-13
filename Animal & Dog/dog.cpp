#include "dog.h"

Dog::Dog() {
    cout << "default dog constructor" << endl;
}
Dog::Dog(string name) : Animal(name) {
    cout << "Dog parameterized constructor" << endl;
}
Dog::~Dog() {
    cout << "Dog destructor" << endl;
}
void Dog::showSpecies() {
    cout << "I'm a dog" << endl;
}