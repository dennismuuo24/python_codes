text = "Hello World!"
print(text[2:5:2]) 
print(text[0])    
print(text*2)
print(text [2])      

#abc[]={"p","r","s"}
#abc[0]="s"
str ="hello world"
new_str="w"+str[0:]
print(new_str)
#print(abc[0])

phone_number = input("Enter a phone number: ")

if len(phone_number) == 10:
    print("Phone number is 10 digits long.")
else:
    print("Phone number is not 10 digits long.")