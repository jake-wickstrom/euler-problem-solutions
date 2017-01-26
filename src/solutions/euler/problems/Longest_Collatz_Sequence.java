package solutions.euler.problems;

public class Longest_Collatz_Sequence {
    static long LARGEST_STARTING_NUMBER = (long) Math.pow(10, 6);

    
    public static long getLongestSequence(){
        long bestStartPoint = 1;
        long longestPathLength = 0;
        long comparePathLength;
        for(long i = LARGEST_STARTING_NUMBER;i>0;i--){
            comparePathLength = collatzSequenceLength(i); 
            if(comparePathLength >longestPathLength){
                bestStartPoint = i;
                longestPathLength = comparePathLength;
            }
        }
        return bestStartPoint;
    }
    
    
    public static long collatzSequenceLength(long startingNum){        
        if(startingNum == 1){
            return 1;
        }else if(startingNum%2==0){
            return 1 + collatzSequenceLength(startingNum/2);
        }else{
            return 1 + collatzSequenceLength(startingNum*3 + 1);
        }
    }
}
