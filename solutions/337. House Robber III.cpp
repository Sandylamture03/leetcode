class Solution {
public:
unordered_map<TreeNode*,pair<int,int>>mp;
void fun(TreeNode* temp)
{
if(temp)
{
fun(temp->left);
fun(temp->right);
if(temp->left==NULL && temp->right==NULL)
mp[temp] = {temp->val,0};
else
{
int r1=0,r2=0,l1=0,l2=0;
if(temp->right) r1 = mp[temp->right].first,r2 = mp[temp->right].second;
if(temp->left) l1 = mp[temp->left].first,l2 = mp[temp->left].second;
mp[temp] = {temp->val+r2+l2,max(l1,l2)+max(r1,r2)};
}
}
}
int rob(TreeNode* root) {
fun(root);
return max(mp[root].first,mp[root].second);
}
};
