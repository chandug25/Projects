# Health Management System
# 3 Clients - Harry, Rohan and Shubham
import datetime
def getdate():
    """"
    the purpose of this function is to give time with every record of food or exercise added in the file
    """
    import datetime
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("Enter 1 for Excersise and 2 for Food"))
        if(c==1):
            value=input("type here\n")
            with open("Harry-ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("Harry-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif(k==2):
        c = int(input("Enter 1 for Excersise and 2 for Food"))
        if (c == 1):
            value = input("type here\n")
            with open("Rohan-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Rohan-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif(k==3):
        c = int(input("Enter 1 for Excersise and 2 for Food"))
        if (c == 1):
            value = input("type here\n")
            with open("Shubham-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Shubham-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter a valid input . i.e, (1(Harry),2(Rohan),3(Shuhbam)")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for Excersise and 2 for Food"))
        if(c==1):
            with open("Harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for Excersise and 2 for Food"))
        if (c == 1):
            with open("Rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for Excersise and 2 for Food"))
        if (c == 1):
            with open("Shubham-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Shubham-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter a valid input (Harry,Rohan,Shubham)")
print("Health Management System: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for Harry 2 for Rohan 3 for Shubham"))
    take(b)
else:
    b = int(input("Press 1 for Harry 2 for Rohan 3 for Shubham"))
    retrieve(b)
