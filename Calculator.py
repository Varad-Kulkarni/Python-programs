import math

def Addition(a,b):
   sum=a+b
   return sum

def Substraction(x,a):
   sub=x-a
   return sub
   
def Multiplication(a,c):
   mult=a*c
   return mult
   
def Division(a,x):
   divs=a/x
   return divs
   
print("select operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.square of number first")
print("6.cube of number first")

while True:

   choice= input("Enter choice(1/2/3/4/5/6): ")
   
   if choice in('1','2','3','4','5','6'):
      num1=float(input("enter first number: "))
      num2=float(input("enter second number: "))
      
      if choice=='1':
         print("Addition of given numbers is: ",Addition(num1,num2))
         
      elif choice=='2':      
         print("Substraction of given numbers is: ",Substraction(num1,num2))
         
      elif choice=='3':   
         print("Multiplication of given numbers is: ",Multiplication(num1,num2))
      
      elif choice=='4':
         print("Division of given numbers is: ",Division(num1,num2))
         
      elif choice=='5':
         print("Square of number first is: ",math.pow(num1,2))

      elif choice=='6':
         print("Cube of number first is: ",math.pow(num1,3))      
      break

   else:
      print("invalid input")   