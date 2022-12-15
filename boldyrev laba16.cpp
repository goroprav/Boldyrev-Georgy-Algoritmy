#include <iostream>
#include <string>
#include <fstream>
#include <stack>

using namespace std;

struct leaf
{
    leaf* left;
    leaf* right;
    int value;
};

class BinaryTree
{
public:

    BinaryTree()
    {
        root = NULL;
    }
    ~BinaryTree()
    {
        delete_tree();
    }

    void delete_tree()
    {
        delete_tree(root);
    }

    void readAndInsert(int& i, string& branch)
    {
        readAndInsert(i, branch, NULL);
    }

    leaf* getRoot()
    {
        return root;
    }

private:

    void delete_tree(leaf* leaf)
    {
        if (leaf != NULL)
        {
            delete_tree(leaf->left);
            delete_tree(leaf->right);
            delete leaf;
        }
    }

    bool readAndInsert(int& i, string& branch, leaf* currentLeaf)
    {
        string str = "";
        while (i < branch.size() && branch[i] != '(' && branch[i] != ')' && branch[i] != ',')
        {
            if (branch[i] != ' ')
            {
                str += branch[i];
            }
            i++;
        }
        i++;

        if (str != "")
        {
            int newValue = stoi(str);

            if (currentLeaf == NULL)
            {
                root = new leaf;
                root->value = newValue;
                currentLeaf = root;
            }
            else
            {
                currentLeaf->value = newValue;
            }
            currentLeaf->left = NULL;
            currentLeaf->right = NULL;

            if (branch[i - 1] != ',' && branch[i - 1] != ')')
            {
                currentLeaf->left = new leaf;
                if (!readAndInsert(i, branch, currentLeaf->left))
                {
                    delete currentLeaf->left;
                    currentLeaf->left = NULL;
                }

                currentLeaf->right = new leaf;
                if (!readAndInsert(i, branch, currentLeaf->right))
                {
                    delete currentLeaf->right;
                    currentLeaf->right = NULL;
                }

            }

            while (i < branch.size() && (branch[i] == ')' || branch[i] == ','))
            {
                i++;
            }
            return true;
        }
        else
        {
            return false;
        }
    }

    leaf* root;
};

int main()
{
    setlocale(LC_ALL, "Russian");
    BinaryTree Tree;

    cout << "Введите значение" << endl;

    string branch;
    getline(cin, branch);
    cout << endl;

    int i = 0;
    Tree.readAndInsert(i, branch);

    stack <leaf*> n_stack;

    n_stack.push(Tree.getRoot());

    leaf* point = n_stack.top();

    while (n_stack.size() > 0)
    {
        while (point != NULL)
        {
            cout << point->value << " ";
            n_stack.push(point);
            point = point->left;
        }

        if (n_stack.top()->right != NULL)
        {
            point = n_stack.top()->right;
        }
        else
        {
            leaf* lastLeaf = n_stack.top();
            n_stack.pop();

            while (n_stack.size() > 0 && (n_stack.top()->right == lastLeaf || n_stack.top()->right == NULL))
            {
                lastLeaf = n_stack.top();
                n_stack.pop();
            }

            if (n_stack.size() < 2)
            {
                break;
            }

            if (n_stack.top()->right != NULL)
            {
                point = n_stack.top()->right;
            }
        }
    }
}