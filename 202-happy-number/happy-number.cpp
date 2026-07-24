class Solution {
public:
    bool isHappy(int n) { 
        int r;
        int s=0;
        if(n==1||n==7) return true;
        else if(n<10) return false;
        else{
           while(n>0){ 
               r=n%10;
               s=s+(r*r);
               n=n/10;
           }
           return isHappy(s);
        }
           

    }
};