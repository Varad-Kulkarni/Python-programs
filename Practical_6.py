str=input("enter string : ")
count = 0
for i in range (0,len(str)):
   if (str[i] != " ") :
      count = count + 1
      
print ( "number of characters in the string is : ",count )
   
funn_dict = {}
dictionari = {} 

for i in range (0,len(str)):
   key = i+1
   value = str [i]
   funn_dict[key] = value

for i in str: 

    if i in dictionari: 
        dictionari[i] += 1
    else: 
        dictionari[i] = 1

print("Number for each character in string is :\n",funn_dict) 
print("Repeated characters in the string are :\n",dictionari)