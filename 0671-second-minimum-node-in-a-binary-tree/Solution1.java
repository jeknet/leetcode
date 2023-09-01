// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int min = -1;
    int min2 = -1;
    boolean wow = false;
    public int findSecondMinimumValue(TreeNode root) {
        if(root == null || root.left == null){
            return -1;
        }
        min = root.val;
        min2 = Integer.MAX_VALUE;
        findMinimums(root); 
        return (min2 == Integer.MAX_VALUE && !wow)?-1:min2;
    }

    private void findMinimums(TreeNode root){
        if(root == null){
            return;
        }

        if(root.val <= min2 && root.val> min){
            min2 = root.val; 
            if(min2 == Integer.MAX_VALUE){
                wow = true;
            }    
        }
        findMinimums(root.left);
        findMinimums(root.right);
    }

}
