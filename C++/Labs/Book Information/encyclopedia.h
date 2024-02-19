#ifndef ENCYCLOPEDIAH
#define ENCYCLOPEDIAH

#include "Book.h"

class Encyclopedia : public Book {
    public:
   // TODO: Declare mutator functions -
   //       SetEdition(), SetNumPages()
        void SetEdition();
        void SetNumPages();

   // TODO: Declare accessor functions -
   //       GetEdition(), GetNumPages()
        string GetEdition();
        string GetNumPages();

   // TODO: Declare a PrintInfo() function that overrides
   //       the PrintInfo() in Book class
    void PrintInfo();

    private:
   // TODO: Declare private data members

};

#endif