#include <iostream>
using namespace std;


int main()
{
    double GPA = 6.9;
    int Age = 18;
    string name = "armaan";

    
    // prints the memory address
    cout << "Age: " << &Age << "\n";
    cout << "GPA: " << &GPA << "\n";
    cout << "Name: " << &name << "\n";

    // can DEREFERENCE a pointer using a * in front
    cout << "Age: " << *&Age << "\n";
    cout << "GPA: " << *&GPA << "\n";
    cout << "Name: " << *&name << "\n";
    
    // variables to store the pointer
    // name should start with &
    // data type should be same
    int *pAge = &Age;
    double *pGPA = &GPA;
    string *pName = &name;

    cout << pAge << "\n";
    cout << pGPA << "\n";
    cout << pName << "\n";

    // can dereference
    cout << *pAge << "\n";
    cout << *pGPA << "\n";
    cout << **&*&*&*&*&*&*&*&*&*&pName << "\n";

    return 0;
}
