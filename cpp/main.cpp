#include<string>
#include<iostream>
#include<vector>
#include"utils.h"

enum checklist
{
    first,
    last
};

int main(){
    std::string a = "sdfsdf";
    print(a.find("df"));
    int b=1;
    int &rel = b;
    b=2;
    //print(b);
    //print(first);
    std::vector<int> dust(1);
    dust[0] = 1;
    dust.push_back(3);
    print(sizeof(dust));
    return 0;
}
