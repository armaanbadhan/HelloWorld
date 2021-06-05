#include <iostream>
using namespace std;


class Book
{
    public:
        string title;
        string author;
        int pages;
    
        Book()
        {
            title = "no title";
            author = "no author";
            pages = 0;
        }

        Book(string aTitle, string aAuthor, int aPages)
        {
            title = aTitle;
            author = aAuthor;
            pages = aPages;
        }
    
};


int main()
{
    Book book1("how to becum dank", "dank memer", 69);

    cout << book1.title << endl;

    Book book2("name 2", "author 2", 345);
    book2.author = "second author";

    cout << book2.author << endl;

    Book book3;
    cout << book3.title << " " << book3.author << "\n";

    return 0;
}
