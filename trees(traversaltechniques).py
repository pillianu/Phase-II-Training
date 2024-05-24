class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printInOrderTraversal(root):
    if root==None:
        return
    printInOrderTraversal(root.left)
    print(root.data,end=" ")
    printInOrderTraversal(root.right)

def printPreOrderTraversal(root):
    if root==None:
        return
    printPreOrderTraversal(root.left)
    print(root.data,end=" ")
    printPreOrderTraversal(root.right)

def levelOrderTraversal(root):
    if root==None:
        return
    result=[]
    Q=[root]

    while len(Q)>0:
        n=len(Q)
        subResut=[]
        for i in range(n):
            #step 1
            currNode=Q.pop(0)
            #step 2
            subResut.append
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj6=Box(60)
obj7=Box(-10)
obj8=Box(100)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
print(printPreOrderTraversal(obj1))
