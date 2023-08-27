// https://leetcode.com/problems/evaluate-boolean-binary-tree/submissions/1033341607/
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
    private Set<Integer> logicOperators = new HashSet<>(Arrays.asList(2,3));
    private Map<Integer, Boolean> booleanVals = Map.of(0, false, 1, true);

    public boolean evaluateTree(TreeNode root) {
        return resolve(root);
    }

    private boolean resolve(TreeNode node){
        if(booleanVals.containsKey(node.val)){
            return booleanVals.get(node.val);
        }
        if(node.val == 2){
            return resolve(node.left) || resolve(node.right);
        }
        return resolve(node.left) && resolve(node.right);
    }
}
