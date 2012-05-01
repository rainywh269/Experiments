#include<iostream>

using namespace std;

int* reverse(int* input){
    int start=i=0, stop=sizeof(input);
    int tmp;
    for(;i<=sizeof(input);i++){
        if(input[i]==3){
            for(;start<=i;start++,stop--) {
                tmp = input[start];
                input[start] = input[stop]
                input[stop] = tmp;
            }
        }
    }

}

void print(int* list){
    int i = 0;
    for(;i<=sizeof(list);i++){
        cout<<list[i]<<endl;
    }
}

int main(){
    int a[] = {1,3,2,2,3,5,6};
    print(a);
}
