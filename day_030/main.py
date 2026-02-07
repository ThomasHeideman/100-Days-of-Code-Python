# KeyError Handling
# We've got some buggy code, try running the code. The code will crash and give you a KeyError.
# This is because some of the posts in the facebook_posts don't have any "Likes".
# Objective:  Use what you've learnt about exception handling to prevent the program from crashing.
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0

    for post in posts:
        try:
            likes = post['Likes']
        except KeyError:
            likes = 0
        total_likes = total_likes + likes

    return total_likes


print(count_likes(facebook_posts))





# # Catch the exception and make sure the code runs without crashing.
# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         fruit = "Fruit"
#     print(fruit + " pie")
#
#
# make_pie(4)



#  FileNotFound
# with open("a file.txt") as file:
#     file.read()

#  KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple","Banana", "Orange"]
# fruit = fruit_list[3]

# TypeError
# text="abc"
# print(text + 5)
#
# try:
# except:
# else:
# finally:
# a_dictionary = {"key": "value"}
# try:
#     file = open("a_text.txt")
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_text.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#      content = file.read()
#      print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error that I made up")


# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# bmi = weight / height **2
# if height > 3:
#     raise ValueError("Heights over 3m are extremely unlikely for humans")
#
# print(bmi)