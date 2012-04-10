#include<iostream>
#include<string>

template <class Type>
void print(Type str){
    std::cout<<str<<std::endl;
}
class C{
    public:
        C(){}
        void Print();
        void Print(int);
        void a(int);
};

void C::a(int a){
    print(a);
}
void C::Print(int a){
    print(a);
}
void C::Print(){
    print("hello");
}

int main(){
    C c =  C();
    try{
        throw C();
    }catch (C){
        print("catchingC");
    }
    c.a(1);
    std::string S = std::string();
    S = "sdfsdfsdf";
    print(S.find("sadf"));
    return 0;
}

