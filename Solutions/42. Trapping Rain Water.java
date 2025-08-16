class Solution {
    public int trap(int[] height) {
        int n = height.length, currentMaxL = 0, currentMaxR = 0, trapped = 0;  

        int leftMaxBoundary[] = new int[n];//getting left max boundary for every ith of column
        leftMaxBoundary[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMaxBoundary[i] = Math.max(height[i], leftMaxBoundary[i - 1]);
        }

        int rightMaxBoundary[] = new int[n];//getting right max boundary for every ith of column
        rightMaxBoundary[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMaxBoundary[i] = Math.max(height[i], rightMaxBoundary[i + 1]);
        }

        for (int i = 1; i < n - 1; i++) { // not including first and last column
            int waterLevel = Math.min(leftMaxBoundary[i], rightMaxBoundary[i]);//determining the water level for particular column on basis farmost boundary
            int trap = waterLevel - height[i];//getting value of trapped water for each column
            trapped += trap;//adding all trapped water
        }
        return trapped;
    }
}
