// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/1036397288/
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        if(root != null){
            return maxDepth(root, 1);
        }
        return 0;
    }

    public int maxDepth(Node node, int level){
        if(node.children != null && !node.children.isEmpty()){
            return Collections.max(node.children.stream().map(n->maxDepth(n, level + 1)).collect(Collectors.toList()));
        }
        return level;
    }
}
