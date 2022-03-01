# # print("chapter 2-3")
# print("one", "two", "three", sep=",")

# print("Hello")
# # print("Hello", end=" ",) # \r
# print("World!")

# #print("a\tb\tc") #a     b   c
# #print("a\tb\tc\nd\te\tf") #a    b   c
#                           #d    e   f

# print('"Hello World!"') # "Hello World!"
# # print(""Hello World!"") # "Hello World!"
# print("\"Hello World!\"") # "Hello World!"
# #print("\Hello World!\")  "Hello World!"
# print("\\Hello World!\\") # "Hello World!"

# print("0123456789012345678901234567")
# print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
# print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep= "")
# print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep= "")
# print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep= "")

#print("{0:<wn}".format(10)) 
#print("There are {0}% probability that the stock market will crash tomorrow!".format(10)) # 10 replace the {0}%
#print("There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!".format(10,50))
# 10 replace the {0}% & 50 replace the {1}%
#str1 = "There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!"
#print(str1.format(10,50))

# print("0123456789012345678901234567")
# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))

# print("0123456789012345678901234567")
# print("{0:^5s}{2:>3s}{1:<20s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{2:>3n}{1:<20s}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{2:>3n}{1:<20s}".format(2, "Hank Aaron", 755))
# print("{0:^5n}{2:>3n}{1:<20s}".format(3, "Babe Ruth", 714))

# print("0123456789012345678901234567")
# print("{0:^5s}{1:^20s}{2:^3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:^20s}{2:^3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{1:^20s}{2:^3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n}{1:^20s}{2:^3n}".format(3, "Babe Ruth", 714))

# print("0123456789012345678901234567")
# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))

#print("The area of {0:s} is {1: ,d} square miles.format("Texas", 268820"))
str2 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str2.format("Texas", 26448000 / 309000000))
# Of the total U.S. population, 8.56% resides in Texas
str2 = "Of the total U.S. population, {1:.2%} resides in Texas."
print(str2.format("Texas", 26448000 / 309000000))

str2 = "Of the total U.S. population, {0:.2%} of households resides in {1:s}".format(26448000 / 309000000, "Texas")

