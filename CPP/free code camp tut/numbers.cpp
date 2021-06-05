#include <iostream>
#include <cmath>
using namespace std;


int main(){
    
    cout << -6541.164 << endl;
    cout << 4-9 << endl;
    cout << 5*8 << endl;
    cout << 8/5 << endl;  // dividing integers gives an integer
    cout << 6%5 << "\n";
    // PEDMAS
    cout << 4 + 5 * 10 << endl;

    int wnum = 5;
    cout << wnum << "\n";
    wnum++;  // += 1;
    cout << wnum << "\n";
    wnum--; // -= 1;
    cout << wnum << "\n";
    wnum = 5;
    cout << wnum++ << "\n";   // first prints then increments
    cout << ++wnum << "\n";   // first increments then prints
    wnum += 80;
    cout << wnum << endl;
    wnum -= 80;
    cout << wnum << endl;

    double a = 9.5;
    int b = 5;
    cout << a + b << "\n"; // gives a decimal

    cout << 10/3 << "\n"; // gives a int
    cout << 10/3.0 << "\n"; // fives a decimal

    cout << pow(4.5, 2) << "\n";  // decimal output
    cout << sqrt(14.3) << "\n";

    cout << round(4.3) << "\n";
    cout << round(4.6) << "\n";

    cout << ceil(4.3) << "\n";
    cout << ceil(4.6) << "\n";

    cout << floor(4.3) << "\n";
    cout << floor(4.6) << "\n";

    cout << fmin(3, 10) << "\n";
    cout << fmax(3, 10) << "\n";

    //exp, log, sin, cos, tan also
    return 0;
}
