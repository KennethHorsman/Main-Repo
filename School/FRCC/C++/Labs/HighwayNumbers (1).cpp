#include <iostream>
using namespace std;

bool IsEven(string highwayNumber) {
    return stoi(highwayNumber) % 2 == 0; // temporarily converts highwaynumber into an int & checks if it evenly divides
}

int main() {
   string highwayNumber, serviceNumber;
   
   cin >> highwayNumber;

   // If invalid highway number (equal to "0", has a "00", or is more than 3 digits)
   if ((highwayNumber.length() == 1 && highwayNumber == "0") || highwayNumber.find("00") != string::npos || highwayNumber.length() > 3) {
      cout << highwayNumber << " is not a valid interstate highway number." << endl;
   }
   
   // If auxiliary highway (3 digits), get service number (two rightmost digits - unless the digit at index 1 is a 0, then the rightmost digit only)
   else if (highwayNumber.length() == 3) {
      serviceNumber = (highwayNumber[1] != '0' ? highwayNumber.substr(1, 2) : highwayNumber.substr(2, 2));
      cout << "I-" << highwayNumber << " is auxiliary, serving I-" << serviceNumber;
      cout << ", going " << (IsEven(highwayNumber) ? "east/west." : "north/south.") << endl;
   }
   
   // If primary highway
   else {
      cout << "I-" << highwayNumber << " is primary, going " << (IsEven(highwayNumber) ? "east/west." : "north/south.") << endl;
   }

   return 0;
}
