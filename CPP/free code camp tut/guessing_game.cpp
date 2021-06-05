#include <iostream>
using namespace std;


int main()
{
    int secretNum = 7, guess = 0, guesscnt = 0, max_guess = 10;

    while (secretNum != guess && guesscnt < max_guess)
    {
        cout << "guess: ";
        cin >> guess;
        guesscnt++;
    }

    if (guesscnt < max_guess)
    {
        cout << "nice" << "\n";
    }
    else
    {
        cout << "loser" << "\n";
    }
    return 0;
}
