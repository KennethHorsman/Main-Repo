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
    void DisplayInfo() const {
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
   string userInput;

   cout << "This program gathers and displays information for one car." << endl;

   Car myCar = CreateCar();
   myCar.DisplayInfo();

   while (askToUpdate) {
        cout << "Would you like to update your car information? Enter 'Y' or 'N'." << endl;
        cin >> userInput;

        if (userInput.length() > 1) cout << "Invalid input given." << endl;
        else {
            userInput = toupper(userInput[0]);

            if (userInput == "Y") {
                myCar = CreateCar();
                myCar.DisplayInfo();
            }
            else if (userInput == "N") askToUpdate = false;
            else cout << "Invalid input given." << endl;
        }
    }

    return 0;
}
