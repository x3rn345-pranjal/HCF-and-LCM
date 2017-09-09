def hcf(a,b):
 
 if(a == b):
    return a
 
 else:
    mx = max(a,b)
    mn = min(a,b)
    a = mn
    b = mx - mn
    return hcf(a,b)
    

a,b = raw_input().split(' ')
a = int(a)
b = int(b)

print hcf(a,b)
lcm = a*b / hcf(a,b)
print lcm


    
    
