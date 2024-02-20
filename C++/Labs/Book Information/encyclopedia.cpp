#include "Encyclopedia.h"
#include <iostream>

// Define functions declared in Encyclopedia.h
void Encyclopedia::SetEdition(string edition) {
    this->edition = edition;
}

void Encyclopedia::SetNumPages(int numPages) {
    this->numPages = numPages;
}

string Encyclopedia::GetEdition() {
    return edition;
}

int Encyclopedia::GetNumPages() {
    return numPages;
}

void Encyclopedia::PrintInfo() {
    Book::PrintInfo();
    cout << "   Edition: " << edition << endl;
    cout << "   Number of Pages: " << numPages << endl;
}

