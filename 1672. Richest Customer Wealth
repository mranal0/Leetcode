int maximumWealth(vector<vector<int>>& accounts)
    {
            int maxWealth = 0;
    for (int i = 0; i < accounts.size(); i++) 
    {
        for (int j = 1; j < accounts[i].size(); ++j) 
        {
            accounts[i][j] += accounts[i][j - 1];  
        }
        int lastIndex = accounts[i].size() - 1;   // Last valid index
        if (maxWealth < accounts[i][lastIndex]) 
        {
            maxWealth = accounts[i][lastIndex];
        }
    }
    return maxWealth;
    }
