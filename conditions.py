#Q.1- Take an input year from user and decide whether it is a leap year or not.
print("CHECK WHETHER A YEAR IS LEAP YEAR OR NOT")
year=int(input("enter the year"))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("%d is a leap year"%(year))
        else:
            print("%d is not a leap year"%(year))
    else:
        print("%d is a leap year"%(year))
else:
    print("%d is not a leap year"%(year))

print("\n\n",10*"*")



#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
print("TO CHECK WHETHER LENGTH AND BREADTH ARE SIDES OF RECTANGLE OR OF SQUARE")
length=input("enter the length")
breadth=input("enter the breadth")
print("length=",length)
print("breadth",breadth)
if (length == breadth):
    print("The above dimensions are sides of square")
else:
    print("The above dimensions are sides of rectangle")

print("\n\n",10*"*")



#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
print("TO FIND THE OLDEST AND YOUNGEST AMONG 3 PEOPLE")
person1=input("enter age of person1:")
person2=input("enter age of person2:")
person3=input("enter age of person3:")
if ((person1 > person2) and (person1 > person3)):
    print(person1,"is oldest")
    if (person2 > person3):
        print(person3,"is youngest")
    else:
        print(person2,"is youngest")
elif((person2 > person1) and (person2 > person3)):
    print(person2,"is oldest")
    if (person1 > person3):
        print(person3,"is youngest")
    else:
        print(person1,"is youngest")
else:
    print(person3,"is oldest")
    if (person1 > person2):
        print(person2,"is youngest")
    else:
        print(person1,"is youngest")

print("\n\n",10*"*")

#Q.4Prize distribution
print("DISTRIBUTION OF PRIZE ACCORDING TO POINTS SCORED")
point=int(input("enter the points scored:"))
if (point > 1 and point <= 50):
    print("Sorry! No prize this time.")
elif (point >50 and point <= 150):
    print("Congratulations! You won a wooden dog")
elif (point >150 and point <= 180):
    print("Congratulations! You won a book")
elif (point >180 and point <= 200):
    print("Congratulations! You won chocolates")
else:
    print("Invalid point! point should be between 1 and 200")


print("\n\n",10*"*")



#Q.5Cost after discount
print("to calculate after discount")
purchase_quantity=int(input("enter the quantity you want to purachase:"))
cost=purchase_quantity*100
if (cost < 1000):
    discount = 0
else:
    discount =0.1 * cost
cost = cost - discount
if (discount == 0):
    print("cost is:",cost)
else:
    print("cost after discount is:",cost)

print("\n\n",10*"*")



    

    

    
   
