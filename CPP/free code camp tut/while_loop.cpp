#include <iostream>
using namespace std;


int main()
{
    /*
    // normal while loop runs 5 times
    int index = 1;
    while (index <= 5)
    {
        cout << index << "\n";
        index++;
    }
    */

   int index = 6;
    
    do{
        cout << index << "\n";
        index++;
    }while (index <= 5);
    //do while loop, will always be executed once, then loop till condition is met
    return 0;
}
