// Modify the TimeHrMn class to utilize a class template. Note that the main() function passes int and double as parameters for the SetTime() member function.

#include <iostream>
using namespace std;

template<typename T>
class TimeHrMn {
public:
    TimeHrMn(T userMin = 0); // Constructor declared
    void SetTime(T userMin);
    void PrintTime() const;
private:
    T hrsVal;
    T minsVal;
};

template<typename T>
TimeHrMn<T>::TimeHrMn(T userMin) {
    SetTime(userMin); // calls SetTime using whichever datatype userMin
}

template<typename T>
void TimeHrMn<T>::SetTime(T userMin) {
    minsVal = userMin;
    hrsVal = userMin / 60; // compiler uses floating point division if userMin double
}

template<typename T>
void TimeHrMn<T>::PrintTime() const {
    cout << "Hours: " << hrsVal << " ";
    cout << "Minutes: " << minsVal << endl;
}

int main() {
    TimeHrMn<int> usrTimeInt;
    TimeHrMn<double> usrTimeDbl;

    usrTimeInt.SetTime(135);
    usrTimeInt.PrintTime();

    usrTimeDbl.SetTime(135.0);
    usrTimeDbl.PrintTime();

    return 0;
}