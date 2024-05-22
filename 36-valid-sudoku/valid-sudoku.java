
class Solution {
    public boolean isValidSudoku(char[][] board) {
           Set exists = new HashSet();
            for(int row = 0;row<9;row++  )
            {
                for (int column = 0; column < 9; column++) {
                    if (board[row][column]!='.') 
                    {
                        String yee = "(" + board[row][column] + ")";
                       if(!exists.add(yee+column)|!exists.add(row+yee)|!exists.add(row/3+yee+column/3)){
                        return false;
                       }
                    }

                }
            }
            return true;

    }
}
