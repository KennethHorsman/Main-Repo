#include "dog.h"
using namespace std;

int Animal::nbrOfAnimals=0;

Animal::Animal() {
    cout << "Animal default constructor" << endl;
    nbrOfAnimals++;
}
Animal::Animal(string name) {
    cout << "Animal parameterized constructor" << endl;
    animalName = name;
    nbrOfAnimals++;
}
Animal::~Animal() {
    cout << "Animal destructor" << endl;
    nbrOfAnimals--;
}
void Animal::setName(string n) {
    animalName = n;
}
string animal::getName() {
    return animalName;
}
int Animal::GetNbrOfAnimals() {
    return nbrOfAnimals;
}
void Animal::showSpecies() {
    cout << "Regular animal" << endl;
}