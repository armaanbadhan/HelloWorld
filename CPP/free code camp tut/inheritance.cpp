#include <iostream>
using namespace std;


class Chef
{
    public:
        void makeChicken()
        {
            cout << "chef makes chicken" << "\n";
        }
        void makeSalad()
        {
            cout << "chef makes a pizza" << "\n";
        }
        void makeSpeicalDish()
        {
            cout << "chef makes something something" << "\n";
        }
};


class ItalianChef : public Chef
{
    // can add and override
    public:
        void makePasta()
        {
            cout << "chef makes pasta" << "\n";
        }
        void makeSpeicalDish()
        {
            cout << "italian chef makes italian pasta" << "\n";
        }
};

/*
Chef class -> super class
ItalianChef -> sub class
*/



int main()
{
    Chef codechef;
    ItalianChef codeforces;
    codechef.makeChicken();
    codeforces.makeChicken();
    codeforces.makePasta();
    //codechef.makePasta(); // gives error

    // can override the function
    codechef.makeSpeicalDish();
    codeforces.makeSpeicalDish();

    return 0;
}
