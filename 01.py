randList = []
[randList.append(i) for i in range(2, 15)]
print(randList)

# a
divisibleList = []
[divisibleList.append(num) if (num % 3 == 0) else [] for num in randList]
print("numbers divisible by 3 are : ", divisibleList)

# b
squares = []
[squares.append(x**2) for x in randList]
print("List of squares", squares)

# c
evenList = []
[evenList.append(i) if (i % 2 == 0) else [] for i in randList]
print("Even List : ", evenList)
sum = 0
[sum := sum+i for i in evenList]
print("Sum of evenlist : ", sum)

# d
reapList = [1, 5, 57, 0, 7, 7]
print("List with duplicate values : ", reapList)
print("Sorted List : ", sorted(list(set(reapList))))
# int object are not iteratable
# [reapList.append(set(i)) for i in range(len(reapList))]
# print(reapList)

# 2
users = {"bob": "admin", "rob": "user 2FA", "jack":
         "user", "jim": "user"}
print("Users on the platform :", users)


def userType(name):
    print(name, "is a :", users.get(name))


userType("bob")
