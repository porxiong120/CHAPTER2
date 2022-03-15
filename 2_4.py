# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3 
# print("Sum is {}".format(sum_of_all_numbers))

# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3 
# print("Sum is {0:s}".format(sum_of_all_numbers))

# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3 
# print("Sum is {0:n}".format(sum_of_all_numbers))

# list_of_numbers = [1, 10, 1000]
# print(sum(list_of_numbers))

# #use loop to add 

# list_of_numbers = [1, 10, 1000]
# print(max(list_of_numbers))

# list_of_numbers = [1, 10, 1000]
# print(min(list_of_numbers))

# list_of_numbers = [1, 10, 1000]
# print(len(list_of_numbers))

# list_of_numbers = [1, 10, 1000]
# print(list_of_numbers.count(4))

# list_of_numbers = [1, 10, 1000]
# print(list_of_numbers.index(1))

# #list_of_numbers = [1, 10, 1000]
# #print(list_of_numbers.reverse())

# list_of_words = ["spam", "ni"]
# print(list_of_words.reverse())


# from audioop import lin2adpcm


# list_of_numbers = [1, 10, 1000]
# print(list_of_numbers)
# list_of_numbers.clear()
# print(list_of_numbers)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# list_of_numbers.append(100)
# print(list_of_numbers)

# Adding/concatenating arrays .extend 
# list_of_numbers2 = [3, 100, 5]
# list_of_numbers3 = list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers)

# # Adding/concatenating arrays using +
# l1 = [1, 32, 4]
# l2 = [100, 200, 300]
# l3 = l1 + l2
# print(l3)

#words = ["Spam", "Wink", "Hi", "My", "In"]
#words.insert(1, "Hello")
#words.insert(-1, "Hello")
#words.insert(len(words), "Hello")
#print("Words=====>", words)


# grades = []
# num = float(input("Enter the first grade: "))
# grades.append(num)
# num = float(input("Enter the second grade: "))
# grades.append(num)
# num = float(input("Enter the third grade: "))
# grades.append(num)
# num = float(input("Enter the fourth grade: "))
# grades.append(num)
# num = float(input("Enter the fifth grade: "))
# grades.append(num)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# average = sum(grades) / len(grades) 
# print("Average Grade: {0:.2f}".format(average))

# grades.append(1)
# grades.append(2)
# grades.append(4)
# grades.append(9)

# print("grades", grades)

# length = len(grades) #
# print("length", length)
# print("sliced:", grades[0:2])
#print("sliced:", grades[0:"2"]) # dont work, "2" is a string

# parts = "a,b,c".split(",")

# print("parts: ", parts)

# str1 = "a,b,c"
# parts = str1.split(",")

# print("parts: ", parts)

# lines = ["To", "be", "or", "not", "to", "be"]
# print("lines before join: ", lines)

#joined = " ".join(lines)
# joined = ",".join(lines)
#joined = "-".join(lines)

# print("joined: ", joined)

# open up the Data.txt file in read mode
# infile = open("Data.txt", "r")
# print("infile", infile)

# #using for loop 2 populate names array with names
# for line in infile: 
#     print("line: ", line.rstrip())
#     print("line after striping the right side: ", line.rstrip())

# # close the Data.txt file to preserve memory 
# infile.close()

# infile = open("Data.txt", "r")
# print("infile", infile)
# names = []
# #using for loop 2 populate names array with names
# for line in infile: 
#     #print("line: ", line.rstrip())
#     #print("line after striping the right side: ", line.rstrip())
#     names.append(line.rstrip())
# print("names: ", names)
# # close the Data.txt file to preserve memory 
# infile.close()

# infile = open("Data.txt", "r")
# print("infile", infile)
# names = []
# #using for loop 2 populate names array with names
# for line in infile: 
#     names.append(line.rstrip())
# #infile.close()

# infile = open("Data.txt", "r")
# names_using_list_comprehesion = [line.rstrip() for line in infile]
# print("names_using_list_comprehension: ", names_using_list_comprehesion)
# # close the Data.txt file to preserve memory 
# infile.close()

# infile = open("Grades.txt", "r")
# for line in infile:
#     print("line: ", line)

# infile.close()

# infile = open("Grades.txt", "r")
# for line in infile:
#     print("line: ", eval(line))

# infile.close()

# infile = open("Grades.txt", "r")
# list_of_numbers = [eval(line) for line in infile]
# print("line: ", list_of_numbers)
# infile.close()

# list_of_names = ("Lucas", "John", "Adam")
# print("list_of_names", list_of_names)

# list_of_names = ("Lucas", "John", "Adam")
# print("list_of_names", list_of_names[1])

# list_of_names = ("Lucas", "John", "Adam")
# print("list_of_names", list_of_names[:])

# list_of_names = ("Lucas", "John", ["A", "B", "C"])
# print("list_of_names", list_of_names[2])

# list_of_names = ("Lucas", "John", ["A", "B", "C"])
# print("list_of_names", list_of_names[2][1])

# list_of_names = ("Lucas", "John", ["A", (1, 2, 3), "C"])
# print("list_of_names", list_of_names[2][1][-1])

# list1 = ["A", "B", "C"]
# list2 = list1
# list2.append("D")
# print(list1)

list1 = ["A", "B", "C"]
list2 = list(list1)
list2.append("D")
print(list1)
