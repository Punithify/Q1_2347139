randList = []

for i in range(2, 15):
    randList.append(i)

print(randList)
# a
divisibleList = []


for num in randList:
    if (num % 3 == 0):
        divisibleList.append(num)

print(divisibleList)

# b
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)

# c
evenList = []
for i in randList:
    if (i % 2 == 0):
        evenList.append(i)
print(evenList)
sum = 0
print([i+i for i in evenList])
for i in evenList:
    sum = sum+i
print(sum)

# d
reapList = [1, 5, 57, 0, 7, 7]
print(set(reapList))


# b
companyDel = {"Virat Kohli": "5 November 1988", "Umesh Yadav": "25 October 1987", "Manish Pandey":
              "10 September 1989", "Rohit Sharma": "30 April 1987", "Ravindra Jadeja": "6 December 1988", "Hardik Pandya": "11 October 1993"}


def brithDate(name):
    print(companyDel.get(name))


brithDate("Virat Kohli")
