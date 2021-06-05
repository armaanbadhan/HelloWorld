#include <iostream>
using namespace std;


double cube(double num)
{
    double res = num * num * num;
    return res;
    cout << "this wont print";
}



int main()
{
    double x = cube(5.5);
    cout << x << endl;
    cout << cube(7.6);
    return 0;
}
