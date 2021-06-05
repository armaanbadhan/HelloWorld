#include <iostream>
using namespace std;


class Book
{
    public:
        string title;
        string author;
        int pages;
    
};




int main()
{
    Book book1;
    book1.title = "CP3";
    book1.author = "someone";
    book1.pages = 1000;

    cout << book1.title;

    Book book2;
    book2.title = "lord of wings";
    book2.author = "dank memer";
    book2.pages = 300;
    book2.author = "hahahahahah";

    cout << book2.author;

    return 0;
}
