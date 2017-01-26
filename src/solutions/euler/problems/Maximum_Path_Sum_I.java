package solutions.euler.problems;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Maximum_Path_Sum_I {
    /*for every point on the path that is passed through, to maximize it should be passed through in the optimal way.
     * the optimal path to a point is the path with the highest sum. It is easy to determine the optimal sum at a point as it
     * is just the highest optimal path value to the two point above plus the value of the point. If we go row by row and
     * calculate the optimal path value for each point, the maximum value on the bottom row will be the absolute maximum value.
     * 
     *  Max(i) = V(i) + Max(Max(left) or Max(right)) Where v(i) is the value at position i;
     *  
     *  For simplicity imagine as a right triangle instead of a pyramid. Entries can only pass down or down and right.
     */
      
        
    
    public static int proveBestPath(String data, int pyramidDepth){
        final int MAX_WIDTH_DEPTH = pyramidDepth;
        File dataFile = new File(data);
        Scanner getData;
        int[][] pyramid = new int[MAX_WIDTH_DEPTH][MAX_WIDTH_DEPTH];
        
        try {
            getData = new Scanner(dataFile);            
            int position = 0;
            int width_depth = 0;
            while(getData.hasNext()){
                pyramid[position][width_depth] = getData.nextInt();
                position++;
                
                if(position> width_depth){
                    width_depth++;
                    position = 0;
                }
            }
            
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
        for(int i=0;i<MAX_WIDTH_DEPTH;i++){
            for(int j = 0;j<MAX_WIDTH_DEPTH;j++){
                if(pyramid[j][i]!=0){
                    if(pyramid[j][i]>9){
                        System.out.print(pyramid[j][i] + " ");
                    }else{
                        System.out.print("0" + pyramid[j][i] + " ");
                    }
                }                               
            }
            System.out.println();
        }
        int x_position = 0;
        int depth = 1; 
                       // since the optimal value at the top of the pyramid is just the height of the pyramid
                       // there is no need to start there
                       //note that the depth of the pyramid is equal to the width at any level.
        
        while(depth!= MAX_WIDTH_DEPTH){
            System.out.println(x_position + "" + depth);
            if(x_position == 0){
              //Any path on the left side must have come from directly above
                pyramid[x_position][depth] = pyramid[x_position][depth -1] + pyramid[x_position][depth]; 
                                                                            
            }else if(x_position == depth){
              //Any path on the right side must have come from above and to the left
                pyramid[x_position][depth] = pyramid[x_position-1][depth -1] + pyramid[x_position][depth];
                
              //Also signals to move to next depth
                depth++;
                x_position = -1; //compensates for the incrementing of x_position at end of method
            }else{ 
                pyramid[x_position][depth] = (pyramid[x_position][depth -1]>pyramid[x_position-1][depth -1])?
                        pyramid[x_position][depth -1] + pyramid[x_position][depth]
                        :pyramid[x_position-1][depth -1] + pyramid[x_position][depth];
            }            
            x_position++;            
        }
        
        /*now the whole pyramid has been converted to its optimal values at each point. We just need to find the greatest
         * optimal value on the bottom row.
         */
        
        int max = 0;
        
        for(int i = 0; i < MAX_WIDTH_DEPTH; i++){
            if(pyramid[i][MAX_WIDTH_DEPTH - 1] > max){
                max = pyramid[i][MAX_WIDTH_DEPTH - 1];
            }            
        }
        
        for(int i=0;i<MAX_WIDTH_DEPTH;i++){
            for(int j = 0;j<MAX_WIDTH_DEPTH;j++){
                if(pyramid[j][i]!=0){
                    if(pyramid[j][i]>9){
                        System.out.print(pyramid[j][i] + " ");
                    }else{
                        System.out.print("0" + pyramid[j][i] + " ");
                    }
                }                               
            }
            System.out.println();
        }
        
        
        return max;
    }
}
