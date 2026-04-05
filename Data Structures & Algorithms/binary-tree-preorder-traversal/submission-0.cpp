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
    vector<int> preorderTraversal(TreeNode* root) {
        
        vector<int> preorder;

        traversal(root, preorder);

        return preorder;

    }

    void traversal(TreeNode* node, vector<int>& path){

        if(node == nullptr){
            return;
        }

        path.push_back(node->val);

        traversal(node->left, path);
        traversal(node->right, path);
    }
};