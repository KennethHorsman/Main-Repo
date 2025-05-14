#include <iostream>
#include <string>
#include "animal.h"
using namespace std;

class Dog : public Animal {
    public:
        Dog();
        Dog(string name);
        ~Dog();
        void showSpecies();
};