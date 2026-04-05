/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        traverse_helper(root);
        return postOrder;
    }

    void traverse_helper(TreeNode* root){
        if(root == nullptr)
            return;

        traverse_helper(root->left);
        traverse_helper(root->right);
        postOrder.push_back(root->val);

    }

    vector<int> postOrder;
};