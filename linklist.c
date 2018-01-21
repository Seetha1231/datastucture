#include<stdio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node* next;
};
void push(struct node** head_ref,int n)
{
	struct node* newn=(struct node*)malloc(sizeof(struct node));
	newn->data=n;
	newn->next=*head_ref;
	*head_ref=newn;
}
void print(struct node* node)
{
	while(node!=NULL)
	{
		printf("%d\t",node->data);
		node=node->next;
	}
}
void insertAfter(struct node** head,int p,int n)
{
		struct node* newn=(struct node*)malloc(sizeof(struct node));
		newn->data=n;
		struct node* head1=*head;
		while(head1->data!=p)
		head1=head1->next;	
		newn->next=head1->next;
		head1->next=newn;
}
void append(struct node** head,int n)
{
		struct node* newn=(struct node*)malloc(sizeof(struct node));
		newn->data=n;
		newn->next=NULL;
		struct node* temp=*head;
		while(temp->next!=NULL)
			temp=temp->next;
		temp->next=newn;
}
void delete(struct node** head,int d)
{
	struct node* temp=*head,*prev;
	if(temp!=NULL && temp->data==d)
	{
		*head=temp->next;
		free(temp);
	}
	while(temp!=NULL && temp->data!=d)
	{
		prev=temp;
		temp=temp->next;
	}
	if(temp==NULL)return;
	prev->next=temp->next;
	free(temp);
}
void deletpos(struct node** head,int p)
{
	int i;
	struct node* temp=*head,*prev;
	prev=temp;
	if(p==0)
	{
		*head=temp->next;
		free(temp);
		return;
	}
	for(i=0; temp!=NULL&&i<p ;i++)
	{
		prev=temp;
		temp=temp->next;
	}
		if(temp==NULL)return;
	prev->next=temp->next;
		free(temp);
}
void swapnode(struct node** head,int x,int y)
{
		struct node *px,*cx,*py,*cy;
		cx=*head;
		while(cx && cx->data!=x)
		{
			px=cx;
			cx=cx->next;
		} 
		cy=*head;
		while(cy && cy->data!=y)
		{
			py=cy;
			cy=cy->next;
		} 
		if(cx==NULL || cy==NULL || x==y) return;
		if(px!=NULL)
		px->next=cy;
		else
		*head=cy;
		if(py!=NULL)
		py->next=cx;
		else
		*head=cx;
		struct node *t=cy->next;
		cy->next=cx->next;
		cx->next=t;		
}
main()
{
	struct node* head=NULL;
	push(&head,5);
		push(&head,15);
			push(&head,25);
			insertAfter(&head,25,10);
			append(&head,120);
			append(&head,100);
			swapnode(&head,5,10);
		//	delete(&head,10);
		//	deletpos(&head,2);
	print(head);
}
