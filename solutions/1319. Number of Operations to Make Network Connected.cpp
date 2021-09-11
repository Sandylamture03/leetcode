class Solution {
public: 
    vector<int>parent;
    int findp(int n)
    {
        if(parent[n]==n)
            return n;
        return parent[n]=findp(parent[n]);
    }
    
​
    int makeConnected(int n, vector<vector<int>>& conn) {
        int siz=conn.size();
​
        parent.resize(n);
        int redundant=0;
        
        for(int i=0;i<n;i++)
        {
            parent[i]=i;
        } 
        int cnt=n;
        for(int i=0;i<siz;i++)
        {
            int el1=conn[i][0];
            int el2=conn[i][1];
            
            int p1=findp(el1);
            int p2=findp(el2);
            
            if(p1!=p2)
            {
                parent[p1]=p2;
                cnt--;
            }
            else
                redundant++;
        }
        
        int toConnect=cnt-1;
        
        if(redundant<toConnect)
            return -1;
        
        return toConnect;
        
        
    }
};
