# LIst Comprehension
# Squared NUmbers

num_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_num = [num ** 2 for num in num_list]
# print(squared_num)

# Filter even numbers

even_num = [num for num in num_list if not num % 2]
# print(even_num)

# Find common numbers in file1 and file2 files

with open("file1.txt") as file:
    file1 = file.readlines()
with open("file2.txt") as file:
    file2 = file.readlines()

common_num = [int(num.strip()) for num in file1 if num in file2]
# print(common_num)

# Dictionary Comprehension

sentence = "What is the Airspeed velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
# print(result)

# Convert temp c to f
weather = {
    "Mon": 12,
    "Tues": 24,
    "Wed": 15,
    "Thurs": 20,
    "Fri": 18,
    "Sat": 22,
    "Sun": 24,
}
weather_f = {day: (temp * 9 / 5) + 32 for day, temp in weather.items()}
print(weather_f)