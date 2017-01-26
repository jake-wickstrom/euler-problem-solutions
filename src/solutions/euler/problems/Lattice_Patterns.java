package solutions.euler.problems;

public class Lattice_Patterns {
        final static int GRID_X_DIMENSION = 21;
        final static int GRID_Y_DIMENSION = 21;
        static long[][] array = new long[GRID_X_DIMENSION][GRID_Y_DIMENSION];
        static int numPaths = 0;
    
        public static long numPaths(){
            //traverses from top left of grid to bottom right
            for(int i = 0;i<GRID_X_DIMENSION;i++){
                array[0][i]=1;
                array[i][0]=1;
            }
            
            for(int i = 1; i<GRID_X_DIMENSION; i++){
                for(int j = 1; j<GRID_Y_DIMENSION; j++){
                    array[i][j]= array[i-1][j]+array[i][j-1];
                }
            }
            return array[20][20];       
    }   
}
