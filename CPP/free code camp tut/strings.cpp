#include <iostream>
using namespace std;


int main(){
    // constant strings
    cout << "hello friends "; // no new line 4 u
    cout << "chai peelo" << endl;
    
    // variable strings
    string name = "armaan";
    cout << name << endl;
    cout << name.length() << endl; // length -> length duh
    cout << name[2] << endl;       // 0 based indexing, can access
    // can change individual char
    name[2] = 'M';
    cout << name << endl;

    cout << name.find('M', 0) << endl; // search 'M' after 0th index
    cout << name.substr(3, 2) << endl; // new substring from index 3, of length 2
    string haha = name.substr(3, 2);   // can store
    cout << haha << endl;
    return 0;
}
