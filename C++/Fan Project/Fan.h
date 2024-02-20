#include <string>

using namespace std;

// Define constants in the global scope
class Fan {
    public:
        Fan(); 
        void setSpeed(int newSpeed); 
        int getSpeed() const; // using const indicates that data is not being modified
        void setState(bool state); 
        bool getState() const; 
        void setRadius(double newRadius); 
        double getRadius() const; 
        void setColor(string newColor); 
        string getColor() const; 
        void displayFan() const; 
        
        static const int SLOW; // static indicates that this data member belongs to the class rather than the instance
        static const int MEDIUM;
        static const int FAST;
    
    private:
        int speed;
        bool isOn;
        double radius;
        string color;
        static int id;
}; // End of class defintion for Fan
