#include <iostream>

using namespace std;

int main(){
    // hello world
    std::cout << "Hello World!" << std::endl;

    // intro to variables
    string CharacterName = "tom";          // <bucket type> <bucket name> = <bucket value>
    int charAge;
    charAge = 20;

    cout << "once there was a man named " << CharacterName << endl;
    cout << "he was " << charAge << " years old" << endl;

    CharacterName = "mike";

    cout << "he liked the name " << CharacterName << endl;
    cout << "but didnt like being " << charAge << endl;

    // data types
    char grade = 'a';
    string phrase = "hello world";
    int age = -90;
    double gpa = 9.2;
    bool isMale = true;
    cout << grade << phrase << age << gpa << isMale <<  endl;
    cout << -4.09 << endl;
    cout << false << endl;
    cout << true << endl;
    cout << 'a' << endl;

    //working with strings
    cout << "giraffe academy";
    cout << "hello world" << endl;      //wont print in new line because last line didnt end
    cout << "giraffe academy\n";        //  '\n' is "enter"
    cout << "hello world" << endl;

    string name = "abcdefghij";
                // 0123456789
    cout << name.length() << endl;
    cout << name[0] <<endl;

    name[0] = 'k';
    cout << name << endl;

    return 0;
}
