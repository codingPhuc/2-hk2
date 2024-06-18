

T=[2,
7,5,
2,6,None,9,
None,None,5,11,None,None,4,None,
None,None,None,None,None,None,'J',None,None,None,'K','L',None,None,None,None]

print(T)

T=[50,
17,76,
9,23,54,None,
None,14,19,None,None,72,None,None,
None,None,12,None,None,None,None,None,None,None,67,None,None,None,None,None]


def list_print(tree_list):
    print(" "+str(tree_list[0]))
    number = 2
    double_number = 4
    for i in range(1,len(tree_list)):
        if tree_list[i] is not None:
            print(str(tree_list[i]),end= ' ')
            
        
        if  i+2 ==double_number: 
            print()
            double_number = double_number*2
            # print(double_number)
            # print(number)
list_print(T)


class bNode(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def tree_creation(root:list):
    tree_root = root[0]

A=bNode(2)
A.left=bNode(7)
A.right=bNode(5)
B=A.left
C=A.right 
B.left = bNode(2)
B.right = bNode(6)
C.right = bNode(9)
D = B.right
D.left = bNode(5)
D.right = bNode(11)
F = C.right 
F.left = bNode(4)


A=bNode('A')
A.left=bNode('B')
A.right=bNode('C')
B=A.left
C=A.right
B.right=bNode('D')
D=B.right
C.left=bNode('E')
C.right=bNode('F')
E=C.left
F=C.right
D.left=bNode('G')
D.right=bNode('H')
E.left=bNode('I')
G=D.left
H=D.right
I=E.left
H.left=bNode('J')
J=H.right
I.left=bNode('K')
I.right=bNode('L')
K=I.left
L=I.right

dict= {'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L }
a= dict[E.left.data]
NoneType = type(None)
if isinstance(A.left.left, NoneType):
    print("True")
    
def NLR(node):
    if isinstance(node, NoneType)!= True:
        print(node.data)
    if isinstance(node.left, NoneType)!= True:
        NLR(dict[node.left.data])  
    if isinstance(node.right, NoneType)!= True: 
        NLR(dict[node.right.data])
NLR(A)
    

    
    