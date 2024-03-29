#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class CarDealership {
private:
    struct Vehicle {
        string make;
        string model;
        string VIN;
        double mileage;
        string color;
        double retailPrice;
        int timeOnLot;
    };

    struct Client {
        string name;
        int age;
        string address;
        int clientId;
    };

    struct SoldVehicle {
        Vehicle vehicle;
        Client client;
        double salePrice;
    };

    vector<Vehicle> vehicles;
    vector<Client> clients;
    vector<SoldVehicle> soldVehicles;

public:
    CarDealership() {}
    virtual ~CarDealership() {}

    // Add vehicle to inventory
    void addVehicle(const string& make, const string& model, const string& VIN,
                    double mileage, const string& color, double retailPrice, int timeOnLot) {
        vehicles.push_back({make, model, VIN, mileage, color, retailPrice, timeOnLot});
    }

    // Add client to list
    void addClient(const string& name, int age, const string& address, int clientId) {
        clients.push_back({name, age, address, clientId});
    }

    // Search for vehicles by make, model, color, and price
    vector<Vehicle> searchVehicles(const string& make, const string& model,
                                    const string& color, double maxPrice) {
        vector<Vehicle> result;
        for (const auto& vehicle : vehicles) {
            if ((make.empty() || vehicle.make == make) &&
                (model.empty() || vehicle.model == model) &&
                (color.empty() || vehicle.color == color) &&
                (maxPrice == 0 || vehicle.retailPrice <= maxPrice)) {
                result.push_back(vehicle);
            }
        }
        return result;
    }

    // Search for client by name and age
    vector<Client> searchClients(const string& name, int age) {
        vector<Client> result;
        for (const auto& client : clients) {
            if ((name.empty() || client.name == name) &&
                (age == 0 || client.age == age)) {
                result.push_back(client);
            }
        }
        return result;
    }
};

int main() {
    CarDealership dealership;

    // Add vehicles to inventory
    dealership.addVehicle("Toyota", "Camry", "123456", 5000, "Blue", 25000, 30);
    dealership.addVehicle("Honda", "Accord", "789012", 8000, "Red", 30000, 40);
    dealership.addVehicle("Toyota", "Corolla", "987654", 6000, "Black", 20000, 25);

    // Add clients to list
    dealership.addClient("John Doe", 35, "123 Main St", 1);
    dealership.addClient("Jane Smith", 40, "456 Elm St", 2);

    // Search for vehicles by user input
    cout << "Enter vehicle details (press Enter if not searching with that parameter):" << endl;
    string make, model, color;
    double maxPrice = 0;
    cout << "Make: ";
    getline(cin, make);
    cout << "Model: ";
    getline(cin, model);
    cout << "Color: ";
    getline(cin, color);
    cout << "Max Price: ";
    cin >> maxPrice;

    vector<CarDealership::Vehicle> searchResults = dealership.searchVehicles(make, model, color, maxPrice);
    cout << "Search Results:" << endl;
    for (const auto& vehicle : searchResults) {
        cout << "Make: " << vehicle.make << ", Model: " << vehicle.model
            << ", Color: " << vehicle.color << ", Price: $" << vehicle.retailPrice << endl;
    }

    // Search for clients by user input
    cin.ignore(); // Clear newline left in buffer after entering maxPrice
    cout << "Enter client details (press Enter if not searching with that parameter):" << endl;
    string name;
    int age = 0;
    cout << "Name: ";
    getline(cin, name);
    cout << "Age: ";
    cin >> age;

    vector<CarDealership::Client> clientSearchResults = dealership.searchClients(name, age);
    cout << "Client Search Results:" << endl;
    for (const auto& client : clientSearchResults) {
        cout << "Name: " << client.name << ", Age: " << client.age
            << ", Address: " << client.address << ", Client ID: " << client.clientId << endl;
    }

    return 0;
}
