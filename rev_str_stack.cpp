#include<iostream>
#include<string>
using namespace std;
struct stack
{
    char data;
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
    void push(char n)
    {
        struct stack *ptr=new stack;
        ptr->data=n;
        ptr->next=NULL;
        if(top!=NULL)
             ptr->next=top;
        top=ptr;
        //cout<<ptr->data;
    }
    char pop()
    {
        if(top==NULL)
        {
        cout<<"Underflow"<<endl;
        return NULL;
        }
        struct stack *temp;
        temp=top;
        char c=temp->data;
        top=top->next;
       // cout<<"\nPopped element :"<<temp->data<<endl;
         delete temp;
         return c;
    }
};
int main()
{
    stac s;
    string nam,p="";
    cout<<"Enter name :";
string st;

	//to avoid an empty string
	getline(cin, st);
 int l=st.length();
	if(l==0 ) {
            cout<<"Oops \nempty string"<<endl;
return 0;
	}
	else{

    int i;
    for(i=0;i<l;i++)
        s.push(st[i]);
    for(i=0;i<l;i++)
        p+=s.pop();
    cout<<"\nReversed string :"<<p<<endl;
}
}
