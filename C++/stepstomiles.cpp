#include <iostream>
#include <iomanip>
#include <stdexcept>

using namespace std;

double StepsToMiles(int steps) {
    if (steps < 0) {
        throw runtime_error("Exception: Negative step count entered.");
    }
    double miles = static_cast<double>(steps) / 2000.0;
    return miles;
}

int main() {
    int steps;
    cin >> steps;

    try {
        double miles = StepsToMiles(steps);
        cout << fixed << setprecision(2);
        cout << miles << endl;
    } catch (runtime_error &e) {
        cout << e.what() << endl;
    }

    return 0;
}