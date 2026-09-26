import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {

        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i = left ; i <= right ; i++){
            int temp = i;
            int flag = 0;

            while(temp > 0){
                int d = temp%10;

                if( d == 0){
                    break;
                }
                if(i%d == 0){
                    flag += 1;
                }else{
                    break;
                }
                temp /= 10;
            }
            if(flag == String.valueOf(Math.abs(i)).length()){
                list.add(i);
            }
        }
        return list;
    }
}