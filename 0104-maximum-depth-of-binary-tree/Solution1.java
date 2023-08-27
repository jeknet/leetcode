// https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1033360330/
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
        Integer counter = 0;
        Map<Integer, Integer> levels = new HashMap();

        addNodesToLevel(levels, 0, root);
        if(levels.keySet().size() > 0){
            return Collections.max(levels.keySet())+1;
        }
        return 0;
    }

    private void addNodesToLevel(Map<Integer, Integer> levels, Integer level, TreeNode node){
        if(node != null){ 
            levels.put(level, levels.getOrDefault(level, 0)+1);
            addNodesToLevel(levels, level+1, node.left);
            addNodesToLevel(levels, level+1, node.right);
        }

    }
}
