class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int inputLength = nums.length;
        int[] result = new int[inputLength];
        int[] left = new int[inputLength];
        int[] right = new int[inputLength]; 
        
        left[0] = 1;
        for(int i = 1;i<inputLength;i++)
        {   
            left[i] = left[i - 1] * nums[i - 1];
        }
        right[inputLength - 1] = 1;
        for (int i = inputLength - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < inputLength; i++) {
            result[i] = left[i] * right[i];
        }
        return result;

    }
}