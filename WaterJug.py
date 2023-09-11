x=0
y=0
m=4
n=3
print("initial state=(0,0)")
print ("Rule 1 : Fill the 4 gallon jug ")
print ("Rule 2: Fill the 3 gallon jug")
print ("Rule 3: Empty the 4 gallon jug")
print ("Rule 4 : Empty the 3 gallon jug ")
print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")
while x!=2:
    r=int(input("Enter rule"))    
    if r==1 :
        print ("Rule 1 : Fill the 4 gallon jug ") 
        x=m
    elif r==2 :
        print ("Rule 2: Fill the 3 gallon jug")
        y=n
    elif r==3 :
        print ("Rule 3: Empty the 4 gallon jug") 
        x=0
    elif r==4 :
        print ("Rule 3: Empty the 4 gallon jug")
        y=0
    elif r==5 :
        print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
        t= n-y
        y=n
        x-=t    
    elif r==6:
        print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
        t= m-x
        x=m
        y -=t
    elif r==7:
        print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
        y=y+x
        x=0
    elif r==8:
        print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")
        x=x+y
        y=0
    print (x,y)
