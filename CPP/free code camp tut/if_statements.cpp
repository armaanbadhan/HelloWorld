#include <iostream>
using namespace std;


int main()
{
    bool isMale = false;
    bool isTall = true;

    if (isMale && isTall)
    {
        cout << "tall male" << "\n";
    }
    else if(isMale && !isTall)
    {
        cout << "tiny male" << "\n";
    }
    else if (!isMale && isTall)
    {
        cout << "tall not male" << "\n";
    }
    else
    {
        cout << "tiny not male" << "\n";
    }
    return 0;
}


/*

    && -> and
    || -> or
    ! -> not

*/