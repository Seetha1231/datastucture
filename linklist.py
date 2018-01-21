
class Node:
	def __init__(self,d):
		self.data=d
		self.next=None


class linkedlist:
	def __init__(self):
		self.head=None
	def push(self,data):
		newnode=Node(data)
		newnode.next=self.head
		self.head=newnode
	def InsertAfter(self,data,prev_data):
		if self.head ==None:
			return
		newnode=Node(data)
		h1=self.head
		try:
			while h1.data!=prev_data :
				h1=h1.next
			newnode.next=h1.next
			h1.next=newnode
		except:
			print (prev_data, ' is Not in a list ')
			return
	def append(self,data):
		newnode=Node(data)
		h1=self.head
		if h1==None :
			newnode=Node(data)
			newnode.next=self.head
			self.head=newnode
			return
		while h1.next!=None :
			h1=h1.next
		newnode.next=h1.next
		h1.next=newnode
	def delete(self,data):
		temp=self.head
		if temp!=None and temp.data==data:
			self.head=temp.next
			temp=None
			return
		while temp!=None and temp.data!=data:
			prev=temp
			temp=temp.next
		if temp==None:
			print(data ,' is Not in a list')
			return
		prev.next=temp.next
		temp=None
	def deletepos(self,index):
		temp=self.head
		try :
			if index==0:
				self.head=temp.next
				temp=None
				return
			for i in range(index):
				prev=temp
				temp=temp.next
			prev.next=temp.next
			temp=None
		except:
			print(index ,'is Out of range')
			return
	def swap(self,x,y):
		cx=self.head
		px,py=None,None
		while cx!=None and cx.data!=x:
			px=cx
			cx=cx.next
		cy=self.head
		while cy!=None and cy.data!=y:
			py=cy
			cy=cy.next
		if x==y or cx==None or cy==None:
			return
		if px!=None :
			px.next=cy
		else :
			self.head=cy
		if py !=None :
			py.next=cx
		else :
			self.head=cx
		t=cy.next
		cy.next=cx.next
		cx.next=t
	def print(self) :
		temp=self.head
		if temp==None :
			print("Underflow")
			return
		while temp!=None:
			print(temp.data,end="\t")
			temp=temp.next
	def unknown(self):
		print('Invalid')
	def reverse(self):
		if(self.head==None):
			return None
		cur=self.head
		prev=None
		while(cur!=None):
			advance=cur.next
			cur.next=prev
			prev=cur
			cur=advance
		self.head=prev
def main():
	l=linkedlist()
	while(True):
		print('\n*******Insertion***********\n[1].Push \n[2].InsertAfter a Number\n[3].Append\n********Deletion*********\n[4].Delete a number\n[5].Delete at position\n[6]Swap 2 Numbers\n[7].Reverse a list\n[8].Print a list\n')
		n=int(input('Enter your choice :'))
		if n==1:
			l.push(int(input('Enter Number :')))
		elif n==2:
			l.InsertAfter(int(input('\nEnter a Number :')),int(input('Enter  previous Number :')))
		elif n==3 :
			l.append(int(input('Enter Number :')))
		elif n==4:
			l.delete(int(input('Enter Number :')))
		elif n==5:
			l.deletepos(int(input('Enter position(from 0) :')))
		elif n==6:
			print('\nBefore Swap :' )
			l.print();
			l.swap((int(input('\nEnter first Number :'))),int(input('Enter  second Number :')))
			print('\nAfter swap   :')
			l.print();
		elif n==7:
			l.reverse()
		elif n==8:
			l.print()
		else:
			l.unknown()
			break
main()