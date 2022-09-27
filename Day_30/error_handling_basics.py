#Exceptions: try(something that might cause an exception ), except(do this if there was an exception), 
# else(do this if there were no exceptions) and finally(do this no matter what happens)


#File not found
# try:
#     file =open("./day_30/data.txt")
#     dict = {"key": "value"}
#     value = dict["key"]
    
# except FileNotFoundError:
#     file = open("./day_30/data.txt", "w")
#     file.write("SOmething")

# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist")

# #Runs when there was no exception in try
# else: 
#     content = file.read()
#     print(content)

# finally:
#     raise KeyError

#Raise - You can raise whereever you want
height = float(input("Height: "))
weight= float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight/height ** 2
print(bmi)

#KeyError
# dict = {"key": "value"}
# value = dict["non_existed_key"]

#INdexError
# list1 = [1,3,5,2,9]
# list_filter = list1[6]

#TypeError
# text="abc"
# print(text+5)






