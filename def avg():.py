def avg():
    global a,b
    sum=a+b
    avg=(sum)/2
    return avg

a=int(input("enter number" ))
b=int(input("enter number" ))
print(avg())