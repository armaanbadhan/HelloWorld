#include <iostream>
using namespace std;


int power(int baseNum, int powNum)
{
    int res = 1;
    for (int i = 0; i < powNum; i++)
    {
        res *= baseNum;
    }
    return res;
}


int main()
{
    cout << power(3, 4);
    return 0;
}
