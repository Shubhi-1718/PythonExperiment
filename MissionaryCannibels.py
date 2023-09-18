m1=3
c1=3
m2=0
c2=0

print("Rules for the game")
print("Rule 1: One Missionary is sailing boat from Bank 1 to Bank 2")
print("Rule 2: Two Missionary are sailing boat from Bank 1 to Bank 2")
print("Rule 3: One Missionary and One Cannibal are selling boat from Bank 1 to Bank 2")
print("Rule 4: One Cannibal is sailing boat from Bank 1 to Bank 2 ")
print("Rule 5: Two Cannibal are sailing boat from Bank 1 to Bank 2 ")
print("Rule 6: One Missionary is sailing boat from Bank 2 to Bank 1")
print("Rule 7: Two Missionary are sailing boat from Bank 2 to Bank 1")
print("Rule 8: One Missionary and One Cannibal are selling boat from Bank 2 to Bank 1")
print("Rule 9: One Cannibal is sailing boat from Bank 2 to Bank 1 ")
print("Rule 10: Two Cannibal are sailing boat from Bank 2 to Bank 1 ")

while (m2!=3) or (c2!=3):
  r=int(input("Enter rule"))
  if r==1:
    print("Rule 1: One Missionary is sailing boat from Bank 1 to Bank 2")
    m1=m1-1
    m2=m2+1
  elif r==2:
    print("Rule 2: Two Missionary are sailing boat from Bank 1 to Bank 2")
    m1=m1-2
    m2=m2+2
  elif r==3:
    print("Rule 3: One Missionary and One Cannibal are selling boat from Bank 1 to Bank 2")
    m1=m1-1
    m2=m2+1
    c1=c1-1
    c2=c2+1
  elif r==4:
    print("Rule 4: One Cannibal is sailing boat from Bank 1 to Bank 2 ")
    c1=c1-1
    c2=c2+1
  elif r==5:
    print("Rule 5: Two Cannibal are sailing boat from Bank 1 to Bank 2 ")
    c1=c1-2
    c2=c2+2
  elif r==6:
    print("Rule 6: One Missionary is sailing boat from Bank 2 to Bank 1")
    m2=m2-1
    m1=m1+1
  elif r==7:
    print("Rule 7: Two Missionary are sailing boat from Bank 2 to Bank 1")
    m2=m2-2
    m1=m1+2
  elif r==8:
    print("Rule 8: One Missionary and One Cannibal are selling boat from Bank 2 to Bank 1")
    m2=m2-1
    m1=m1+1
    c2=c2-1
    c1=c1+1
  elif r==9:
    print("Rule 9: One Cannibal is sailing boat from Bank 2 to Bank 1 ")
    c2=c2-1
    c1=c1+1
  elif r==10:
    print("Rule 10: Two Cannibal are sailing boat from Bank 2 to Bank 1 ")
    c2=c2-2
    c1=c1+2
  print(m1,c1) 
  print(m2,c2)
  if ((m1>0 and m1<c1) or (m2>0 and m2<c2)): 
    print("Cannibals eat the missionaries")
    break 
