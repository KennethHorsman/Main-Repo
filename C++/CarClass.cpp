#include <iostream>
#include <string>

using namespace std;

class Car {
public:
    // Constructor with string model and string make parameters
    Car(string model, string make) : carModel(model), carMake(make) {} // This initalizes the variables without adding extra lines

    // Getter methods to acess data members from Main()
    string GetModel() const { // const indicates that these methods to not modify any attributes
        return carModel;
    }

    string GetMake() const {
        return carMake;
    }

    // Setter methods to change the car attributes
    void SetModel(string newModel) {
        carModel = newModel;
    }

    void SetMake(string newMake) {
        carMake = newMake;
    }

    // Method to display information about the car
    void DisplayInfo() const {
        cout << "Car Information: " << carMake << " " << carModel << endl;
    }

private:
    string carModel;
    string carMake;
};

Car CreateCar() { // Made a function to create a car object, reducing redundant code
   string inputMake, inputModel;

   cout << "Enter Make of Car: ";
   getline(cin, inputMake); // There is an automatic newline after this
   cout << "Enter Model of Car: ";
   getline(cin, inputModel);

   return Car(inputModel, inputMake);
}

int main() {
   bool askToUpdate = true;
   string userInput; // Using string vs char prevents possible errors if the user enters more than one character

   cout << "This program gathers and displays information for one car." << endl;

   Car myCar = CreateCar();
   myCar.DisplayInfo();

   while (askToUpdate) {
        cout << "Would you like to update your car information? Enter 'Y' or 'N': ";
        getline(cin, userInput); // For some reason, using "cin >>" here makes it skip getting input for model of car when Y is entered. Fixed w/ "cin.ignore()" though.

        if (userInput.length() > 1) cout << "Invalid input given." << endl; // Verifies the string is one charcter to prevent any issues. If not, repeats the loop.
        else {
            userInput = toupper(userInput[0]); // toupper only works on a single character. This allows user to accidentally enter a lowercase Y or N.

            if (userInput == "Y") {
                myCar = CreateCar(); // An alternative to this is changing the Setter methods to take input and calling them individually
                cout << "Updated ";
                myCar.DisplayInfo();
            }
            else if (userInput == "N") askToUpdate = false; // Exits loop when the user is satisfied with their car information
            else cout << "Invalid input given." << endl; // States an error message, repeats the loop
        }
    }
    
    cout << "Enjoy your " << myCar.GetMake() << " " << myCar.GetModel() << "!" << endl; // Example of using Getting or Setter function

    return 0;
}
