#include <iostream>
using namespace std;


int main()
{
    int numbergrid[3][2] = {{1, 2}, {3, 4}, {5, 6}};
    //cout << numbergrid[0][0] << endl;
    //cout << numbergrid[2][1] << endl;
    //cout << numbergrid[1][1] << endl;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << numbergrid[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
