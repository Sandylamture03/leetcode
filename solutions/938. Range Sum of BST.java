/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        findSum(root, low, high);
        return sum;
    }
    
    private void findSum(TreeNode root, int low, int high) {
        if(root == null) {
            return;
        }
        
        boolean left = root!=null && root.val >= low;
        if(left) {
             findSum(root.left, low, high);
        }
        
        boolean right = root!=null && root.val <= high;
        if(right) {
             findSum(root.right, low, high);
        }
        
        if(left && right) {
            sum = sum + root.val;
        }
        
    }
}
