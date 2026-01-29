# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# print(programming_dictionary["Loop"])
#
# for key in programming_dictionary:
#     print(key + ': ' + programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
   if student_scores[key] <= 70:
       student_grades[key]="Fail"
   elif 71 <= student_scores[key] <=80 :
       student_grades[key]="Acceptable"
   elif 81 <= student_scores[key] <=90 :
       student_grades[key]="Exceeds Expectations"
   elif 91 <= student_scores[key] <=100 :
       student_grades[key]="Outstanding"

print(student_grades)
