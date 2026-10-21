# r=5
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# Output:

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 


# r=5
# for i in range(1,r+1):
#      print("* "*i)

# Output :
# * 
# * * 
# * * * 
# * * * * 
# * * * * *


# r=5
# for i in range(r, 0 , -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Output

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# r=5
# for i in range(r, 0, -1):
#      print("* "*i)

# Output:

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


# r=5

# for i in range(1, r+1):
#     print(" " * (r-i), end="")
#     print("*" + " " * (2*i-3) + "*" if i > 1 else "*")


# for i in range(r-1, 0, -1):
#     print(" " * (r-i), end="")
#     print("*" + " " * (2*i-3) + "*" if i > 1 else "*")

# second: 

# lines = 5

# # Upper part
# for j in range(lines):
#     print(" " * (lines - 1 - j), end="")
    
#     if j == 0:
#         print("*")
#     else:
#         print("*" + " " * (2*j - 1) + "*")

# # Lower part
# for j in range(lines - 2, -1, -1):
#     print(" " * (lines - 1 - j), end="")
    
#     if j == 0:
#         print("*")
#     else:
#         print("*" + " " * (2*j - 1) + "*")

# Output 

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

lines=5

for j in range(lines):
    print(" "*((lines-1)-j),"* "*(j+1))
for j in range(1,lines):
    print(" "*j,(lines-j)*"* ")

# output:

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      * 