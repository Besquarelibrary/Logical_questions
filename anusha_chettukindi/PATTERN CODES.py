QUESTION: PATTERN-1
-------------------------
# # # # # # # # 

# # #     # # # 

# #         # # 

#             # 

#             # 

# #         # # 

# # #     # # # 

# # # # # # # # 
LOGIC-1

for i in range(0,8):
    for j in range(0,8):
        if((i==0 or i==7) and j<=7) or ((j==0 or j==7) and i<=7):
            print("# ",end="")
        elif((i==1 and (1<=j<3 or (5<=j<7))) or (i==6 and (1<=j<3 or (5<=j<7)))):
            print("# ",end="")
        elif((i==2 or i==5) and (j==1 or j==6)):
            print("# ",end="")
        else:
            print("  ",end="")
            
    print("\n")
------------------
LOGIC-2:
for i in range(0,8):
    for j in range(0,8):
        if((i==0 or i==7) and j<=7) or ((j==0 or j==7) and i<=7):
            print("# ",end="")
        elif((j==1 or j==6) and i!=3 and i!=4):
            print("# ",end="")
        elif((i==1 or i==6) and (j==2 or j==5)):
            print("# ",end="")
        else:
            print("  ",end="")
            
    print("\n")
---------------------------------------------------------------------------------------
PATTERN-2:

#             # 

# #         # # 

# # #     # # # 
# # # # # # # # 

# # #     # # # 

# #         # # 

#             # 
---------------
LOGIC

for i in range(0,7):
    for j in range(0,8):
        if(((j==0 or j==7) and (i<=6))or(i==3 and j<=7)):
            print("# ",end="")
        elif((j==1 or j==6) and ((1<=i<3) or (4<=i<6))):
            print("# ",end="")
        elif((i==2 or i==4) and (j==2 or j==5)):
            print("# ",end="")
        else:
            print("  ",end="")
    print("\n")

---------------------------------------------------------------------------------------------
PATTERN-3

        A 

      A B A 

    A B C B A 

  A B C D C B A 

A B C D E D C B A
--------------------
LOGIC 
-----------------------
n=8//2
for i in range(0,5):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(chr(65+k),end=" ")
    for l in range(i,0,-1):
        print(chr(65+l-1),end=" ")
        
    print("\n")
--------------------------------------------------------------------------------
PATTERN-4

      1 

    2 1 2 

  3 2 1 2 3 

4 3 2 1 2 3 4 
 
-----------------
LOGIC
-----------------
for i in range(0,4):
    for k in range(0,4-i-1):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    for k in range(1,i+1):
        print(k+1,end=" ")
    print("\n")
-------------------------------------------------------------------------
PATTERN-5

1             1 

1 2         2 1 

1 2 3     3 2 1 

1 2 3 4 4 3 2 1 
------------------------

LOGIC

for i in range(0,4):
    for j in range(0,i+1):
        print(j+1 ,end=" ")
    for k in range(0,4-i-1):
        print("  ",end="  ")
    for l in range(i+1,0,-1):
        print(l ,end=" ")
    print("\n")
------------------------------------------------------------------------------------------------
PATTERN-6

A             A 

A B         B A 

A B C     C B A 

A B C D D C B A 
-------------
LOGIC
-------------
for i in range(0,4):
    for j in range(0,i+1):
        print(chr(65+j),end=" ")
    for k in range(0,4-i-1):
        print("  ",end="  ")
    for l in range(i+1,0,-1):
        print(chr(65+l-1),end=" ")
    print("\n")
---------------------------------------------------------------------------------------------------
