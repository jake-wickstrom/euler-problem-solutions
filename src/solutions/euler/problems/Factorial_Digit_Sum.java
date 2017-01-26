package solutions.euler.problems;

public class Factorial_Digit_Sum {
    static int[] factorialTracker = new int[1000];
    
    public static long getFactorialSum(){
        factorialTracker[0]=1;
        
        for(int i = 1; i <= 100; i++){
            for(int j = 0; j < factorialTracker.length; j++){
                factorialTracker[j]*=i;
            }
            update();
        }
        
        long sum = 0;
        for(int j = 0; j < factorialTracker.length; j++){
            sum+=factorialTracker[j];
        }
        
        return sum;
        
    }
    
    private static void update(){
        for(int i=0;i<factorialTracker.length;i++){
            if(factorialTracker[i] >= 10){
                factorialTracker[i+1] += factorialTracker[i]/10;
                factorialTracker[i] = factorialTracker[i]%10;
            }
        }
    }
}
