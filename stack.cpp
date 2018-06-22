#include<iostream>
using namespace std;
struct stack
{
    int data;
    struct stack *next;
};

class stac
{
    struct stack *top;
public:
    stac()
    {
        top=NULL;
    }
    void push(int n)
    {
        struct stack *ptr=new stack;
        ptr->data=n;
        ptr->next=NULL;
        if(top!=NULL)
             ptr->next=top;
        top=ptr;
        //cout<<ptr->data;
    }
    void pop()
    {
        if(top==NULL)
        {
        cout<<"Underflow"<<endl;
        return ;
        }
        struct stack *temp;
        temp=top;
        top=top->next;
        cout<<"\nPopped element :"<<temp->data<<endl;
         delete temp;
    }
    void show()
    {
        struct stack* s=top;
        while(s!=NULL)
        {
            cout<<s->data<<"\t";
            s=s->next;
        }
    }
};

int main()
{
    stac s;
    int ch,n;
    while(1)
    {
        cout<<"[1].push\n[2].pop\n[3].show\n";
        cin>>ch;
        switch(ch)
        {
        case 1:
            cout<<"Enter n :";
            cin>>n;
            s.push(n);
            break;
        case 2:
            s.pop();
            break;
        case 3:
            s.show();
            break;
        }
    }
return 0;

}
