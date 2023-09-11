jug1=0
jug2=0
jug1cap=4
jug2cap=3
print("initial state=(0,0)")
print ("Rule 1 : Fill the 4 gallon jug ")
print ("Rule 2: Fill the 3 gallon jug")
print ("Rule 3: Empty the 4 gallon jug")
print ("Rule 4 : Empty the 3 gallon jug ")
print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")
while jug1!=2:
    r=int(input("Enter rule"))    
    if r==1 :
        print ("Rule 1 : Fill the 4 gallon jug ") 
        jug1=jug1cap
    elif r==2 :
        print ("Rule 2: Fill the 3 gallon jug")
        jug2=jug2cap
    elif r==3 :
        print ("Rule 3: Empty the 4 gallon jug") 
        jug1=0
    elif r==4 :
        print ("Rule 3: Empty the 4 gallon jug")
        jug2=0
    elif r==5 :
        print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
        jug1=jug1-(jug2cap-jug2)
        jug2=jug2cap
    elif r==6:
        print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
        jug2=jug2-(jug1cap-jug1)
        jug1=jug1cap
    elif r==7:
        print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
        jug2=jug2+jug1
        jug1=0
    elif r==8:
        print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")
        jug1=jug1+jug2
        jug2=0
    print (jug1,jug2)

