#include<stdbool.h>
bool isPalindrome(int x) {
    int long num=x;
    int long lastdigit,rev=0;
    while(num>0){
        lastdigit=num%10;
        rev=10*rev+lastdigit;
        num/=10;
    }
    if(x==rev){
        return 1;
    } else {
        return 0;
    }    
}