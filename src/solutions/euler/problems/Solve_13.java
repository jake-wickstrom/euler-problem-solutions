package solutions.euler.problems;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solve_13 {
    /*
     * Rep: Each digit of a number is represented as an integer in an array, where the array index is equivilant to the digits position in the number.
     * RI: No index contains a number greater than 9.
     * Abstraction function: AF(n)= sum of sumTracker[i]*10^i for all i in array 
     */
    private static int[] sumTracker = new int[100];
    private static char[] currentNumRep = new char[50];
    private static int[] currentNum = new int[50];
    
    public static String first_10(){
        String digits = new String();
        File numbersFile = new File("Data/numbers.txt");
        
        try {
            Scanner getNum = new Scanner(numbersFile);
            while(getNum.hasNextLine()){
                currentNumRep = getNum.nextLine().toCharArray();
                int index = currentNumRep.length - 1;
                for(char a : currentNumRep){
                    currentNum[index] = Character.digit(a,10);
                    index--;                
                }
                for(int i = 0; i<50; i++){
                    sumTracker[i]+=currentNum[i];
                }
                update();
            }
            getNum.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
        int k = 0;
        int i = 99;
        boolean foundFirstZero = false;
        while(k < 10 && i > 0){
            if(sumTracker [i] !=0 || foundFirstZero){
                //System.out.print(sumTracker[i] + " (" + k +") ");
                digits = digits.concat(Integer.toString(sumTracker[i]));
                foundFirstZero = true;
                k++;        
            }
            i--;
        }
        return digits;
    }
    
    private static void update(){
        for(int i = 0; i < 100; i++){
            if(sumTracker[i]>= 10){
                sumTracker[i]-=10;
                sumTracker[i+1]++;
            }
        }
    }
}

