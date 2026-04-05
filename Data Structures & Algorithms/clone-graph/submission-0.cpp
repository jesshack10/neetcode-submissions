/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
               
        if(node == nullptr) return nullptr;

        queue<Node*> q;
        unordered_map<Node*, Node*> cloned;

        cloned[node] = new Node(node->val);
        q.push(node);

        while(!q.empty()){

            auto n = q.front();
            q.pop();
            
            for(const auto neighbor : n->neighbors){
                if(cloned.count(neighbor) == 0){
                    cloned[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }

                cloned[n]->neighbors.push_back(cloned[neighbor]);
            }

        }

        return cloned[node];
    }
};
