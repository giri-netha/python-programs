class stack():
    def __init__(self):
        self.l=[]
    def push(self,element):
        self.l.append(element)
    def pop(self):
        if(len(self.l)==0):
            print(-1)
        else:
            print(self.l.pop(),end=" ")
    def peek(self):
        if(Stack.isEmpty()):
            print("Stack is empty..")
        else:
            print(self.l[-1])
    def isEmpty(self):
        if len(self.l) == 0:
            return True
        return False
    def size(self):
        return len(self.l)
    

Stack = stack()
print(Stack.isEmpty())
for i in range(4):
	Stack.push(input("enter the string:"))
for i in range(2):
    Stack.pop()
print()
print(Stack.isEmpty())
print(Stack.size())
Stack.peek()
