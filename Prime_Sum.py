#Write a program to find first n prime numbers and the sum

def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  
  
N=int(input("Enter N:"))  
i=2 
lst=[] 
while(1):  
    if(Prime(i)):  
        lst.append(i) 
        if(len(lst)==N): 
            break 
    i+=1 
print("First "+str(N)+" Prime numbers are:",end="") 
print(*lst)

MAX = 10000
prime = [True for i in range(MAX + 1)]
def SieveOfEratosthenes():
 
    prime[1] = False
 
    for p in range(2, MAX + 1):
 
        if (prime[p] == True):

            i = p * 2
            while(i <= MAX):
                prime[i] = False
                i = i + p
                
def solve( n):

    count = 0
    num = 1

    total = 0
 
    while (count < n+1):
 
        if ( prime[num] ):
            total = total + num

            count = count + 1
 
        num = num + 1
     
    return total

SieveOfEratosthenes()
 
n = 4

print("Sum of 1st N prime " +
      "numbers are :", solve(n))
 