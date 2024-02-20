#ifndef ENCYCLOPEDIAH
#define ENCYCLOPEDIAH

#include "Book.h"

class Encyclopedia : public Book {
       public:
   // TODO: Declare mutator functions -
   //       SetEdition(), SetNumPages()
       void SetEdition(string edition);
       void SetNumPages(int numPages);

   // TODO: Declare accessor functions -
   //       GetEdition(), GetNumPages()
       string GetEdition();
       int GetNumPages();

   // TODO: Declare a PrintInfo() function that overrides
   //       the PrintInfo() in Book class
       void PrintInfo();

       private:
   // TODO: Declare private data members
       string eTitle;
       string eAuthor;
       string ePublisher;
       string ePublicationDate;
       string edition;
       int numPages;

};

#endif