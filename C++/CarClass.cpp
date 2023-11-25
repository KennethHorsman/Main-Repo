#include <iostream>
#include <string>

using namespace std;

class Car {
public:
    // Constructor with string model and string make parameters
    Car(string model, string make) : model(model), make(make) {}

    // Getter methods to acess data members from Main()
    string getModel() const {
        return model;
    }

    string getMake() const {
        return make;
    }

    // Setter methods to change the car attributes
    void setModel(string newModel) {
        model = newModel;
    }

    void setMake(string newMake) {
        make = newMake;
    }

    // Method to display information about the car
    void displayInfo() const {
        cout << "Car Information: " << make << " " << model << endl;
    }

private:
    string model;
    string make;
};

Car CreateCar() {
   string inputMake, inputModel;

   cout << "Enter Make of Car: ";
   getline(cin, inputMake);
   cout << "Enter Model of Car: ";
   getline(cin, inputModel);

   return Car(inputModel, inputMake);
}

int main() {
   bool askToUpdate = true;

   cout << "This program gathers and displays information for one car." << endl;

   Car myCar = CreateCar();
   myCar.displayInfo();

   while (askToUpdate) {
    cout << "Would you like to update your car information?" << endl;
   }
   cout << "Would you like to update your car information?" << endl;
    // Loop here





   // // Creating a Car object with a string model and string make
   // Car my_car("Civic", "Honda");

   // // Using public method to display information
   // my_car.displayInfo();  // Output: Car Information: Honda Civic

   // // Changing the car using setter methods and variables instead
   // string newModel = "Accord";
   // string newMake = "Toyota
   // ";
   // my_car.setModel(newModel);
   // my_car.setMake(newMake);

   // // Displaying updated information using getters instead
   // cout << "New Car Information: " << my_car.getMake() << " " << my_car.getModel() << endl;

    return 0;
}
