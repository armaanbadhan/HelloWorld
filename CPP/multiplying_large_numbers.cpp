#include <bits/stdc++.h>
using namespace std;
#define i_am_speed ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long

int main(){
    i_am_speed;
    int a = 1234;
    int ar[20];
    int i = 0;
    while(a){
        ar[i] = a%10;
        a = a/10;
        i++;
    }
    
    return 0;
}