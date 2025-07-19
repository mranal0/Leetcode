// minPrice → keeps track of the lowest price seen so far 
// maxProfit → keeps track of the highest profit possible.

class Solution 
{
    public static int maxProfit(int prices[]) 
    {
        int n = prices.length;
        int minPrice = prices[0];
        int maxProfit = 0;
        for (int i = 0; i < n; i++) 
        {
            minPrice = Math.min(prices[i], minPrice);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        return maxProfit;
    }

}
