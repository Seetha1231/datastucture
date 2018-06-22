#include<iostream>
using namespace std;
class bstree
{
    struct bst{
        int no;
        struct bst* left;
        struct bst* right;
    } ;
    struct bst *root;
          void preord(struct bst* root)
    {
        if(root==NULL)
            return;
        cout<<root->no<<"\t";
        preord(root->left);
        preord(root->right);
    }
         void inord(struct bst* root)
    {
        if(root==NULL)
            return;
        inord(root->left);
        cout<<root->no<<"\t";
        inord(root->right);

    }
          void postord(struct bst* root)
    {
        if(root==NULL)
            return;
        postord(root->left);
        postord(root->right);
    cout<<root->no<<"\t";
    }

public:
    bstree()
    {
        root=NULL;
    }
    bool isEmpty()
    {
        return root==NULL;
    }
    void insert(int n)
    {
        struct bst* b=new bst();
        struct bst* parent=NULL;
        b->no=n;
        b->left=NULL;
        b->right=NULL;
        if(isEmpty())
        {
            root=b;
            return;
        }
        struct bst* cur=root;
        while(cur)
        {
            parent=cur;
            if(n>cur->no)
                cur=cur->right;
            else
                cur=cur->left;
        }
        if(parent->no<n)
        {
            parent->right=b;
        }
        else
            parent->left=b;


    }
    void preorder()
    {
        preord(root);
    }
    void inorder()
    {
        inord(root);
    }
        void postorder()
    {
        postord(root);
    }
};

int main()
{
    bstree b;
    int ch,n;
    while(1)
    {
        cout<<"\n[1].insert\n[2].inorder\n[3].Preorder\n[4].Post order\n[5].exit\n";
        cin>>ch;
        switch(ch)
        {
        case 1:
            cout<<"Enter n:";
            cin>>n;
            b.insert(n);
            break;
        case 2:
            b.inorder();
            break;
        case 3:
            b.preorder();
            break;
        case 4:
            b.postorder();
            break;
        case 5:
            return 0;
        }
    }

}
