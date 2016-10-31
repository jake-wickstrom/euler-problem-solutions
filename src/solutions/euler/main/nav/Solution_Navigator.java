package solutions.euler.main.nav;

import java.util.Scanner;

import solutions.euler.problems.*;

public class Solution_Navigator {
    
    final static int FIRST_PROBLEM_SOLVED = 13;
    final static int LAST_PROBLEM_SOLVED = 18;


    public static void main(String[] args) {
        boolean keepRunning = true;
        //System.out.println(Longest_Collatz_Sequence.collatzSequenceLength(13));
        while(keepRunning){
            System.out.print("Enter a number between " + FIRST_PROBLEM_SOLVED + " and " 
                    + LAST_PROBLEM_SOLVED + " to see the solution to that problem, or -1 to exit:");
            
            Scanner chooseProblem = new Scanner(System.in);
            int problem = chooseProblem.nextInt();
            
            switch (problem){
                case -1: keepRunning = false;
                         break;
                
                case 13: System.out.println(Solve_13.first_10());
                         break;
                         
                case 14: System.out.println(Longest_Collatz_Sequence.getLongestSequence());
                         break;
                         
                case 15: System.out.println(Lattice_Patterns.numPaths());
                         break;
                         
                case 16: System.out.println(Power_Digit_Sum.two_pow_1000());
                         break;
                         
                case 17: System.out.println(Number_Letter_Counts.getTotalWordCount());
                         break;
                         
                case 18: System.out.println(Maximum_Path_Sum_I.proveBestPath("Data/Problem_18_data.txt",15));               
                         break;
                         
                case 67: System.out.println(Maximum_Path_Sum_I.proveBestPath("Data/Problem_67_data.txt",100));
            }
            if(!keepRunning){
                chooseProblem.close();
            }
        }
    }
}
