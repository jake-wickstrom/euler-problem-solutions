package solutions.euler.problems;

public class Power_Digit_Sum {
    
    public static long two_pow_1000(){
        int[] digits = new int[1000];
        digits[0] = 2;
        
        for(int i = 1; i<1000;i++){
            update(digits);
            for(int j = 0; j<1000;j++){
                //System.out.print(digits[j] + " ");
                digits[j]*=2;
            }
            System.out.println();
        }
        update(digits);
        long sum = 0;
        
        for(int i : digits){
            sum += i;
        }
        return sum;
    }
        
    static void update(int[] digits){
        for(int i = 0; i < digits.length; i++){
            if(digits[i]>= 10){
                digits[i]-=10;
                digits[i+1]++;
            }
        }
    }
}
