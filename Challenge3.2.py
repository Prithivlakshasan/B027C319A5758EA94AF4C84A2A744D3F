# 3.2 implement a function called sort students that takes a list of student objects as input and sorts the list based on their CGPA(Cumulative Grade Point Average) in descending order.each student object has the following attributes: name(string),roll number(string), and cgpa(float).test the function with different input lists of student

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_lists):
  #Sort the list of  students in descending order of CGPA
  sorted_students = sorted(student_lists,
                          key=lambda student: student.cgpa,
                          reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students

#Example usage:
students = [
  Student("karthikeyan", "A40", 9.9),
  Student("suriya", "A41", 7.5),
  Student("vaithis", "A42", 8.5),
  Student("veejay", "A43", 9.0),
]

sorted_students = sort_students(students)

# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))
