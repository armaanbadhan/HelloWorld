#include <iostream>
using namespace std;


int main(){

    /*double age;
    cout << "Enter your age: ";
    cin >> age;
    cout << "You are " << age << " years old.";*/

    string name;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Hello " << name;
    return 0;
}
