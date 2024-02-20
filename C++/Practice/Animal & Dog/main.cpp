#include <iostream>
#include "dog.h"
using namespace std;

int main() {
    Animal myAnimal;
    Animal* myAnimal2 = new Animal("Animal 2");
    myAnimal.setName("Animal 1");
    Dog myDog("Dog 1");

    cout << myAnimal2->getNbrOfAnimals() << endl;
    cout << myAnimal.getName() << endl;
    myAnimal.showSpecies();

    cout << myAnimal2->getName() << endl;
    myAnimal2->showSpecies();
    delete myAnimal2;
    cout << myAnimal.getNbrOfAnimals() << endl;

    cout << myDog.getName() << endl;
    myDog.showSpecies();
}