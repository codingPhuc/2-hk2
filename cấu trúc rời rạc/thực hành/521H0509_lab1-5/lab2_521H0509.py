import itertools
import pandas as pd
def function_lImples(P,Q):
    if P==True and Q== False : 
        return False 
    return True 
def function_lAnd(P ,Q) : 
    if P == False  or Q == False :
        return False 
    return True
def function_lXor(P ,Q):
    if P == Q : 
        return False 
    return True 
def function_lLor(P,Q) : 
    if P == True  or Q == True :
        return True 
    return False
def function_lLNot(P):
    if P == True:
        return False 
    return True 
def function_lEquivalent(P ,Q):
    if P == Q : 
        return True 
    return False 


# ex 2 
def function_AlImples(P ,Q) : 
    R =  []
    for i in range(0 ,len(P)):
        R.append(function_lImples(P[i], Q[i]))
    return R 

def function_AlAnd(P ,Q) : 
    R =  []
    for i in range(0 ,len(P)):
        R.append(function_AlAnd (P[i], Q[i]))
    return R 

def function_AlXor(P ,Q) : 
    R =  []
    for i in range(0 ,len(P)):
        R.append(function_AlXor (P[i], Q[i]))
    return R 

def function_AlNot(P ) : 
    R =  []
    for i in range(0 ,len(P)):
        R.append(function_AlNot (P[i]))
    return R 

def function_AlEquivalent(P ,Q) : 
    R =  []
    for i in range(0 ,len(P)):
        R.append(function_lEquivalent (P[i], Q[i]))
    return R   


 
P = [True , True , False , False]
Q = [True , False , True , False]       

            

table = list(itertools.product([False,True],repeat=3))
R  = []
P = []
Q = []
for i  in table : 
    P.append(i[0])
    Q.append(i[1])
    R.append(i[2])

def ex3_1(p, q,r):
    list = []
    for  i in range(0 , len(p)) :
        
        
        if(function_lImples(function_lAnd(p[i],q[i]) , r[i])):
            
            list.append(True)
        else :
            list.append(False)

        
    return list


# ex4.2 
def ex3_2(p, q,r):
    list = []
    for  i in range(0 , len(p)) :
        
        
        if(function_lImples(r[i] , function_lAnd(p[i],q[i]))): 
            
            list.append(True)
        else :
            list.append(False)
    return list 
# ex4  
def ex4_1(p, q):
    list = []
    for  i in range(0 , len(p)) :
        pvq = function_lAnd(p[i],q[i])
        p_q  = function_lLor(p[i],q[i])
        not_pVq =function_lAnd(function_lLNot(p[i]),function_lLNot(q[i]))
        list.append(function_lImples(function_lImples(p_q, pvq), not_pVq))
    return list 
def ex4_2(p, q,r):
    list = []
    for  i in range(0 , len(p)) :
        q_or_r  = function_lLor(q[i],r[i])
        notp_and_q_or_r = function_lAnd(function_lLNot(p[i]), q_or_r) 
        list.append(function_lImples(notp_and_q_or_r, r[i]))
    return list 
def ex4_3(p, q,r):
    list = []
    for  i in range(0 , len(p)) :
          
        list.append(function_lLor(function_lImples(p[i], q[i]), function_lImples(q[i],r[i])))
    return list 
def ex4_4(p, q,r):
    list = []
    for  i in range(0 , len(p)) :
        p_and_qorR = function_lAnd(p, function_lLor(q[i],r[i]))
        pandq_or_pandr = function_lLor(function_lAnd(p[i],q[i]),function_lAnd(p[i],r[i]))
        
          
        list.append(function_lXor(p_and_qorR, pandq_or_pandr))
    return list 
def print_table(q, p, r, ex,name):
    print("Q \t  P \t R \t"  + name)
    print("-------------------------------------")
    for i in range(len(q)):
        print(str(q[i]) + "\t" + str(p[i]) + "\t" + str(r[i]) + "\t" + str(ex[i]))


print_table(Q,P ,R , ex3_1(P,Q,R),"p ∧ q → r")
print_table(Q,P ,R , ex3_2(P,Q,R)," r-> p ∧ q ")
print_table(Q,P ,R , ex4_1(P,Q)," p ∨ q → p ∧ q → ¬p ∨ ¬q")
print_table(Q,P ,R , ex4_2(P,Q,R)," ¬p ∨ (q ∧ r) → r")
print_table(Q,P ,R , ex4_3(P,Q,R)," (p → q) ∧ (q → r)")
print_table(Q,P ,R , ex4_4(P,Q,R),"(p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r))")

# four dif 

table = list(itertools.product([False,True],repeat=4))
R  = []
P = []
Q = []
T = []
for i  in table : 
    P.append(i[0])
    Q.append(i[1])
    R.append(i[2])
    T.append(i[3])
    
def print_table(q, p, r,t, ex,name):
    print("Q \t  P \t R \t T \t"   + name)
    print("-------------------------------------")
    for i in range(len(q)):
        print(str(q[i]) + "\t" + str(p[i]) + "\t" + str(r[i]) + "\t" +str(r[i])+  "\t" + str(ex[i]))



def ex4_5(p, q,r,t):
    list = []
    for  i in range(0 , len(p)) :
        list.append(function_lImples(function_lAnd(p[i],q[i]),function_lAnd(function_lLNot(r[i]),t[i])) )
    return list 
def ex4_6(p, q,r,t):
    list = []
    for  i in range(0 , len(p)) :
        pandt_imples_q = function_lImples(function_lAnd(p[i],t[i]),q[i] )
        
        list.append(function_lImples(pandt_imples_q,function_lImples(r[i],t[i])) )
    return list 
print_table(Q,P ,R,T , ex4_5(P,Q,R,T),"p ∨ q → ¬r ∨ t")
print_table(Q,P ,R,T , ex4_6(P,Q,R,T),"p ∨ t → q → (r → t)")


#ex5 
def ex5_1(p ,q): 
    if(function_lEquivalent(p, function_lLNot(function_lLNot(q)))):
        return "equivalent"
    else:
        return "Inequivalent"  

def ex5_2(p ,q): 
    p_q = function_lLNot(function_lLor(function_lLNot(q),p))
    
    if(function_lEquivalent( function_lEquivalent(function_lLor(p_q),function_lAnd(q,p)),q )):
        return "equivalent"
    else:
        return "Inequivalent"  

def ex5_3(p ,q): 
    p_q = function_lLNot(function_lAnd(p,q))
    not_p_q = function_lAnd(function_lLNot(p),function_lLNot(q))
    if(function_lEquivalent(p_q, not_p_q)):
        return "equivalent"
    else:
        return "Inequivalent"  
def ex5_4(p,q,r ):
    p_q_r =  function_lImples(function_lAnd(p,q) , r)
    not_p_q = function_lAnd(function_lImples(p,r), function_lImples(q,r))
    if(function_lEquivalent(p_q_r, not_p_q)):
        return "equivalent"
    else:
        return "Inequivalent"
    
def ex5_5(p,q,r ):
    p_q_r = function_lLNot(function_lLor(p,q))
    not_p_q = function_lLor(function_lLNot(p) ,function_lLNot(q))
    if(function_lEquivalent(p_q_r, not_p_q)):
        return "equivalent"
    else:
        return "Inequivalent"
    
def ex5_7(p,q,r ):
    p_q_r = function_lLNot(function_lAnd(p,q))
    not_p_q = function_lLor(function_lLNot(p) ,function_lLNot(q))
    if(function_lEquivalent(p_q_r, not_p_q)):
        return "equivalent"
    else:
        return "Inequivalent"


