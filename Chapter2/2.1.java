/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root == NULL)
            return true;
        queue<TreeNode*> lq, rq;
        if(root->left != NULL)
            lq.push(root->left);
        if(root->right != NULL)
            rq.push(root->right);
        TreeNode *l, *r;
        while(!lq.empty() && !rq.empty()) {
            l = lq.front();
            lq.pop();
            r = rq.front();
            rq.pop();
            if(l == NULL && r == NULL)
                continue;
            if(l == NULL || r == NULL || l->val != r->val)
                return false;
            lq.push(l->left);
            rq.push(r->right);
            lq.push(l->right);
            rq.push(r->left);
        }
        if(lq.empty() && rq.empty())
            return true;
        else
            return false;
        
    }
};
