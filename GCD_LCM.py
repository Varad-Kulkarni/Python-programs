num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)
def findlcm(a, b):  
    if(a > b):   
        maximum = a
    else:
        maximum = b
    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm
lcm = findlcm(num1, num2)  
print("LCM is", lcm)