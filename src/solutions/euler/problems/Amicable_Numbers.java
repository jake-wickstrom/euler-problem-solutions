package solutions.euler.problems;

import java.util.HashMap;
import java.util.Map;

public class Amicable_Numbers {
    
    public static int getAmicableSum(){
        
        int AmicableSum = 0;
        Map<Integer,Integer> d_n = new HashMap<Integer,Integer>();
        
        for(int i = 1; i<=10000; i++){
            d_n.put(i, getDivisorSum(i));
        }
        
        for(int num : d_n.keySet()){            
            if(d_n.containsKey(d_n.get(num))){
                if(num == d_n.get(d_n.get(num)) && num != d_n.get(num)){
                    //System.out.println("It's amicable" + num);
                    AmicableSum += num;
                    System.out.println(num + " " + d_n.get(num));
                }
            }
        }
        return AmicableSum;
    }
    
    private static int getDivisorSum(int num){
        int divisorSum = 0;
        for(int i = 1; i<num;i++){
            if(num%i==0){
                divisorSum += i;
            }
        }
        return divisorSum;
    }

}
