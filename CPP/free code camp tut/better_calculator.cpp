#include <iostream>
using namespace std;


int main()
{
    int num1, num2;
    char op;

    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter operator: ";
    cin >> op;
    cout << "Enter second number: ";
    cin >> num2;

    if(op == '+')
    {
        cout << num1+num2 << "\n";
    }
    else if (op == '-')
    {
        cout << num1 - num2 << "\n";
    }
    else if (op == '*')
    {
        cout << num1 * num2 << "\n";
    }
    else if (op == '/')
    {
        cout << num1 / num2 << "\n";
    }
    else
    {
        cout << "not a valid operator\n";
    }

    return 0;
}
