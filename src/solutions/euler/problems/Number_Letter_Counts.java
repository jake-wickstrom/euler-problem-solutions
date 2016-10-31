package solutions.euler.problems;

public class Number_Letter_Counts {
    final static int[] one_nineteen = {3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};
    final static String[] one_nineteen_words = {"one","two","three","four","five","six",
                "seven","eight","nine","ten","eleven","twelve","thirteen","fourteen",
                "fifteen","sixteen","seventeen","eighteen","nineteen"};
    final static String[] multiples_of_ten_words = {"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"};
    final static int and = 3;
    final static int hundred = 7;
    final static int thousand = 8;
    static int currentNumLength = 0;
    static int wordSum = 0;
    
    public static long getTotalWordCount(){
        
        for(int i = 1; i < 1000; i++){
            
            int numTracker = i;
            currentNumLength = 0;
            
    
            if(numTracker>=100){
                currentNumLength += one_nineteen_words[numTracker/100 -1].length() + hundred;
                System.out.print(one_nineteen_words[numTracker/100 -1] + " hundred ");
                numTracker-=(numTracker/100)*100;
                
                if(numTracker!=0){
                    
                    if(numTracker%100<20){
                        currentNumLength += one_nineteen[numTracker%100 -1] + and;
                        System.out.print("and " + one_nineteen_words[numTracker%100 -1]);
                    }else if(numTracker%10!=0){
                        currentNumLength += one_nineteen_words[numTracker%10-1].length();
                        int tempStore = numTracker%10-1;
                        numTracker-=numTracker%10;
                        numTracker/=10;
                        currentNumLength += multiples_of_ten_words[numTracker-2].length() + and;
                        System.out.print("and " + multiples_of_ten_words[numTracker-2] + " " +one_nineteen_words[tempStore]);
                    }else{
                        currentNumLength += multiples_of_ten_words[numTracker/10-2].length() + and;
                        System.out.print("and " + multiples_of_ten_words[numTracker/10-2]);
                    }
                }
            }else{
                if(numTracker%100<20){
                    currentNumLength += one_nineteen_words[numTracker%100 -1].length();
                    System.out.print(one_nineteen_words[numTracker%100 -1]);
                }else if(numTracker%10!=0){
                    currentNumLength += one_nineteen_words[numTracker%10-1].length();
                    int tempStore = numTracker%10-1;
                    numTracker-=numTracker%10;
                    numTracker/=10;
                    currentNumLength += multiples_of_ten_words[numTracker-2].length();
                    System.out.print(multiples_of_ten_words[numTracker-2]+ " " + one_nineteen_words[tempStore]);
                }else{
                    currentNumLength += multiples_of_ten_words[numTracker/10-2].length();
                    System.out.print(multiples_of_ten_words[numTracker/10-2]);
                }
            }
            wordSum += currentNumLength;
            System.out.print( "   " + currentNumLength + " " + wordSum);
            System.out.println();
        }
        return wordSum + one_nineteen_words[0].length() + thousand;
    }
}
