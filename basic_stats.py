# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/02/2024
# Description: Write a class called Student that has two private data members - the student's name and grade.
import statistics
class Student:
    def __init__(self, name, grade, grade):
        self.name = name # Private data member for student's name
        self.grade = grade # Private data member for student's grade
    def get_grade(self):
        return self.grade
def basic_states (student_list):
    grade = [student.get_grade() for student in student_list]
    mean_value = statistics.mean(grades)
    median_value = statistics.median(grades)
    mode_value = statistics.mode(grades)
    return (mean_value, median_value, mode_value)