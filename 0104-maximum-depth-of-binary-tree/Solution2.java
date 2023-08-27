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
    public int maxDepth(TreeNode root) {
        return addNodesToLevel(0, 0, root);
    }

    private Integer addNodesToLevel(Integer counter, Integer level, TreeNode node){
        if(node != null){  
            counter = Math.max(counter, addNodesToLevel(counter, level+1, node.left));
            counter = Math.max(counter, addNodesToLevel(counter, level+1, node.right));
            return counter;
        }
        return level;
    }
}
