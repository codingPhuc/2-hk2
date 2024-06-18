
def extended_gcd(a,b):
    if(b==0): 
        return a, 1, 0
    else :
        gcd , x1 ,y1 = extended_gcd(b , a%b)
        x = y1 
        y  = x1 -(a//b)*y1  
        return gcd  , x , y
def InverseModulo(invert_num : int ,mod_num : int):
    gcb, x, y = extended_gcd(invert_num , mod_num)
    if(gcb != 1):
        return "error" 
    else :
        return x%mod_num
print("this is the inverse mod of number 27 mod 392 ",format(InverseModulo(27,392)))



print("this is the inverse mod of number 888 mod 54",format(InverseModulo(888,54)))


    
    
    
    
