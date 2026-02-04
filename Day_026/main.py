# region LIST COMPREHENSIONS
#  new list = [new_item for item in list]
#  new list = [new_item for item in list if test]
import random

# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# list_comprehension = [n + 1 for n in numbers]
# print(list_comprehension)
#
# new_numbers = [n *2 for n in range(1,5)]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
# short_names = [nme for nme in names if len(nme) <= 4]
# long_names = [nme.upper() for nme in names if len(nme) > 5]

# with open("file1.txt", mode="r") as file:
#     list_1= [int(line.strip("\n")) for line in file]
#
# with open("file2.txt", mode="r") as file:
#     list_2 = [int(line.strip("\n")) for line in file]
#
# result = [n for n in list_1 if n in list_2]
# print(result)
# endregion

#  region DICTIONARY COMPREHENSIONS
#   new_dict = {new_key: new_value for item in list},
#   new_dict = {new_key: new_value for (key,value) in dict.items()},
#   new_dict = {new_key: new_value for (key,value) in dict.items() if test},

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]
# students_scores =  {item: random.randint(1,100) for item in names}
# print(students_scores)
# passed_students = {student: score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_of_words = sentence.split()
#
# result = {word: len(word) for word in list_of_words}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: (temp * 9/5) + 32 for (day,temp) in weather_c.items()}
# print(weather_f)

# endregion

# region How to Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Prikkel","Matisse", "Bob" ],
    "score": [85,92,54]
}
#  looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_dataframe= pandas.DataFrame(student_dict)
# print(student_dataframe)

# loop through a dataframe
# for (key,value) in student_dataframe.items():
#     print(key)
#     print(value)
# loop through rows of a dataframe
for (index,row) in student_dataframe.iterrows():
    if row.student == "Prikkel":
        print(row.score)