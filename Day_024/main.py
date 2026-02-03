# with open("my_file.txt", mode="a+") as file:
#     file.write("\nI a son and I have two cats.")
#     file.seek(0)
#     contents = file.read()
#     print(contents)
#
# with open("new_file.txt", mode="a+") as file:
#     file.write("This is a newly created file.")
#     file.seek(0)
#     contents = file.read()
#     print(contents)

with open("../../../OneDrive/Desktop/new_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
