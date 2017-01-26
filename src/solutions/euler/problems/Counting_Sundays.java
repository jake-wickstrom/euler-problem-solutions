package solutions.euler.problems;

public class Counting_Sundays {
    private static int day = 7; // the first of january 1900 was a Monday, so the first Sunday occurred 6 days later on the 7th
    private static int month = 0;
    private static int year = 1900;
    
    private static int LEAP_FEBUARY = 29;
    private static int REGULAR_FEBUARY = 28;
    private static int DAYS_IN_WEEK = 7;
    
    //1900 is the starting year, which is not a leap year, so febuary starts with 28 days
    final static int[] monthLength = {31,28,31,30,31,30,31,31,30,31,30,31};
    
    public static int getSundays(){
        int sundayTheFirstCount = 0;
      
        while(year == 1900){
            cycle();
            update();
        }
        
        while(year != 2001){
            cycle();
            update();
            sundayTheFirstCount += validSunday();
        }
        
        return sundayTheFirstCount;
        
        
    }
    
    private static void cycle(){
        day+=DAYS_IN_WEEK;
    }
    
    private static void update(){
        if(day>monthLength[month]){
            day-=monthLength[month];
            month++;
        }
        
        //febuary occurs in the first index of the array since january is in index 0
        if(month == 1){
            if((year%4 == 0 && !(year%100 == 0)) || year%400 == 0){
                monthLength[1] = LEAP_FEBUARY; 
            }else{
                monthLength[1] = REGULAR_FEBUARY;
            }
        }
        
        if(month>=12){
            month = 0;
            year++;
        }
    }
    
    private static int validSunday(){
        if (day == 1){
            return 1;
        }
        return 0;
    }
}
