#include <iostream>
using namespace std;


void hiUser(string name, int age)
{
    cout << "Hi " << name << endl;
    cout << "youre " << age << " Years old" << endl;
}


// cant directly put a function below main, should declare it above if defined below main
void sayHi();


// code in main function gets executed by default
// all other functions should be called
int main()
{
    cout << "top" << "\n";
    sayHi();
    hiUser("Armaan", 18);
    cout << "bottom" << "\n";
    return 0;
}


void sayHi()
{
    cout << "Hello User!\n";
}
