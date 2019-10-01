def add(x,y):
    z=x+y
    print(z) 
def isprime(n):
    fact=0
    for i in range(1,n+1):
        if(n%i==0):
            fact=fact+1
    if(fact==2):
        return True
    else:
        return False
isprime(6)        
def primefactors(n):
    if isprime(n)==True:
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")
primefactors(7)                