#include <iostream>
using namespace std;


class Movie
{
    private:
        string rating;
    public:
        string title;
        string director;
        Movie(string atitle, string adirector, string arating)
        {
            title = atitle;
            director = adirector;
            setRating(arating);
        }

        void setRating(string aRating)
        {
            if (aRating == "G" || aRating == "PG" || aRating == "PG-13" || aRating == "R")
            {
                rating = aRating;
            }
            else
            {
                rating = "NR";
            }
        }

        string getRating()
        {
            return rating;
        }
};


int main()
{
    Movie movie1("race 3", "selmon bhai", "PG-13");

    // rating is set private can no longer directly access it
    // movie1. rating = "0/10"; // wont work
    // cout << movie1.rating << endl; // cant print
    // can only be accesses inside the function
    // or through the functions

    cout << movie1.getRating() << endl;
    movie1.setRating("0 / 10");
    cout << movie1.getRating() << endl;
    movie1.setRating("PG");
    cout << movie1.getRating() << endl;
    return 0;
}
