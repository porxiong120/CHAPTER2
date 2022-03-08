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


grades = []
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)
minimumGrade = min(grades)
grades.remove(minimumGrade)
minimumGrade = min(grades)
grades.remove(minimumGrade)
average = sum(grades) / len(grades) 
print("Average Grade: {0:.2f}".format(average))
