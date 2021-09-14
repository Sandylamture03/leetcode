class Solution {
public:
    int sumNumbers(TreeNode* root,int ans=0) {
     if(!root)return 0;
     if(!root->left&&!root->right)return ans*10+root->val;
     return sumNumbers(root->left,ans*10+root->val)+sumNumbers(root->right,ans*10+root->val);
    }
};
