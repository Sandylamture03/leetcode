class Solution {
public:
    
    void inorder(TreeNode *root, vector<int>&vec)
    {
        if(!root)
            return;
        
        inorder(root->left,vec);
        vec.push_back(root->val);
        inorder(root->right,vec);        
    }
    
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int>ans;
        inorder(root1,ans);
        inorder(root2,ans);
        sort(ans.begin(),ans.end());
        return ans;
        
    }
};
