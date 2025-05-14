#include <iostream>
#include <string>
using namespace std;

class Animal {
    protected:
        string animalName;
        static int nbrOfAnimals;
    public:
        Animal();
        Animal(string name);

        ~Animal();

        void setName(string n);
        string getName();
        int getNbrOfAnimals();

        void showSpecies();
};