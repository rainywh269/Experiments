#include<iostream>
#include<string>
#include "../utils.cpp"

using namespace std;

class Aclass{
public: 
    Aclass(){};
    Aclass(int value){
        this->value = value;
    };
    Aclass operator +(Aclass& c1){
        Aclass tmp;
        tmp.value  = value+c1.value;
        return tmp;
    }
    operator int(){
        return value;
    }
    int value;
};

int main(){
    Aclass a1 = Aclass(1);
    Aclass a2 = Aclass(2);
    print(a1+a2);

    return 0;
}
