/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
    if (!root) return [];
    let ar1 = []
    if (root.left) {
        ar1 = ar1.concat(inorderTraversal(root.left));
    }
    ar1.push(root.val);
    if (root.right) {
        ar1 = ar1.concat(inorderTraversal(root.right));
    }
    return ar1;
};


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
    if (!root) {
        return []
    }

    return [...inorderTraversal(root.left), root.val, ...inorderTraversal(root.right)]
};