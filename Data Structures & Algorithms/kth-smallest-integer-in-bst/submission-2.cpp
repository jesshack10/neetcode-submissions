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
    int kthSmallest(TreeNode* root, int k) {
        
        vector<int> kth;
        function<void(TreeNode*,int)> bfs = [&](TreeNode* node, int currk)-> void {

            if(node == nullptr){
                return;
            }

            bfs(node->left, currk + 1);
            kth.push_back(node->val);
            bfs(node->right, currk + 1);
        };

        bfs(root, 0);

        return kth[k - 1];
    }
};
