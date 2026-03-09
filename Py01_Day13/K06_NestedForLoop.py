#K06_NestedForLoop.py

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

##  Soru – Asagidaki sekilleri yazdirin
##  *           * * * * * * * *       * * * * * * * *
##  * *         * * * * * * * *       * * * * * *
##  * * *       * * * * * * * *       * * * *
##  * * * *     * * * * * * * *       * *

##for i in range(1, 5):
##    print("* " * i)
##
##for i in range(1, 5):
##    for j in range(i):
##        print("*", end=" ")
##    print()

## for i in range(4):
##     print("* " * 8)
##
## print()
##
## for i in range(4):
##     for j in range(8):
##         print("*", end=" ")
##     print()
##

for i in range(8, 1, -2):
    print("* " * i)

for i in range(8, 1, -2):
    for j in range(i):
        print("*", end=" ")
    print()