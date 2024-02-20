#include <string>

using namespace std;

// Define constants in the global scope
const int SLOW;
const int MEDIUM;
const int FAST;

class Fan {
    public:
        Fan(); 
        void setSpeed(int newSpeed); 
        int getSpeed() const; 
        void setState(bool newOn); 
        bool getState() const; 
        void setRadius(double newRadius); 
        double getRadius() const; 
        void setColor(string &newColor); 
        string getColor() const; 
        void displayFan() const; 
    
    private:
        int speed;
        bool isOn;
        double radius;
        string color;
        static int id;
}; // End of class defintion for Fan
